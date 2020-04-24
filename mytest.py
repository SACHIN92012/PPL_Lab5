import sys
# from inspect import signature
from typing import TextIO

from antlr4 import *
from gen.java9Lexer import java9Lexer
# from CListener import CListener
from gen.java9Parser import java9Parser
from gen.java9Visitor import java9Visitor
import json
import re
import ast
import copy
import json
import pprint

contextList = []


# Main visitor class
class Myjava9Visitor(java9Visitor):

    def __init__(self):
        self.nodeCounter = 1
        self.textdict = {}
        self.crude_cfg = ""
        self.VarList = []
        self.mainDictionary={"children":[{"import":[],"nodeType":"Imports"}]}
        self.level=0
        self.child_no=1
        self.typeDictionary={}
        self.init_Dict()
    count1=0;

    # Initialising main type dictionary
    def init_Dict(self):
        self.typeDictionary['int'] = {"attributes": {"name": "int", "type": "Integer"}, "name": "BuiltInTypeName"}
        self.typeDictionary['float'] = {"attributes": {"name": "float", "type": "float"}, "name": "BuiltInTypeName"}
        self.typeDictionary['String']={"attributes": {"name": "String", "type": "String"}, "name": "BuiltInTypeName"}
        self.typeDictionary['char']={"attributes": {"name": "char", "type": "char"}, "name": "BuiltInTypeName"}

    # Function for getting Import related details
    def visitTypeImportOnDemandDeclaration(self, ctx:java9Parser.TypeImportOnDemandDeclarationContext):
        a=len(ctx.children)
        s=""
        for i in range(1,a-1):
            s=s+ctx.children[i].getText()
        self.mainDictionary["children"][0]["import"].append(s)

    # Function for checking while statements and getting their details
    def add_while_statement(self,ctx:java9Parser.WhileStatementContext):
        dict={"children":[],"name":"WhileStatement"}
        a=self.cal_Expression(ctx.children[2])
        dict["children"].append(a)
        a=self.block_statement_constructor(ctx.children[4],0)
        dict["children"].append(a)
        return dict

    # Function for checking D0-while statements and getting their details
    def add_DoWhile_statement(self,ctx:java9Parser.DoStatementContext):
        dict={"children":[],"name":"DoWhileStatement"}
        a=self.cal_Expression(ctx.children[4])
        dict["children"].append(a)
        a=self.block_statement_constructor(ctx.children[1],0)
        dict["children"].append(a)
        return dict

    # Function for checking If-Else statements and getting their details
    def add_ifelse_statement(self,ctx:java9Parser.IfThenElseStatementContext):
        dict={"children":[],"name":"IfStatement"}
        dict2=self.cal_Expression(ctx.children[2])
        dict["children"].append(dict2)
        dict2=self.block_statement_constructor(ctx.children[4],0)
        dict["children"].append(dict2)
        if len(ctx.children)==7:
            dict2=self.block_statement_constructor(ctx.children[6],0)
            dict["children"].append(dict2)
        return dict

    # Function for checking For loop statements and getting their details
    def add_for_loop(self,ctx:java9Parser.BasicForStatementContext):
        dict={"children":[],"name":"ForStatement"}
        queue=[ctx]
        while len(queue):
            s=queue.pop(0)
            if type(s) is java9Parser.ForInitContext or type(s) is java9Parser.ForUpdateContext:
                a=self.block_statement_constructor(s,1)
                for node in a:
                    if node is not None:
                        dict["children"].append(node)
                continue
            if type(s) is java9Parser.ExpressionContext:
                a=self.cal_Expression(s)
                dict["children"].append(a)
                continue
            if type(s) is java9Parser.StatementContext:
                a=self.block_statement_constructor(s,0)
                dict["children"].append(a)
                continue
            if hasattr(s, 'children'):
                if s.children is not None:
                    for node in s.children:
                        # print(node.getText())
                        queue.append(node)
        return dict

    # function for adding parameters to the functions and constructors
    def add_parameterlist(self,ctx:java9Parser.FormalParameterListContext):
        dict={"children":[],"name":"ParameterList"}
        dict2={"constant":"false","name":"","value":"null","visibility":"internal","type":""}
        queue=[ctx]
        while len(queue):
            s=queue.pop(0)
            if type(s) is java9Parser.FormalParameterContext:
                dict3={"attributes":{"constant":"false","value":"null","visibility":"internal"},"children":[],"name":"VariableDeclaration"}
                type1=""
                stack=[s]
                identifier1=[]
                while len(stack):
                    p=stack.pop()
                    # print(type(p))
                    if type(p) is java9Parser.VariableModifierContext:
                        if p.getText()=="final":
                            dict3["attributes"]["constant"] = "true"
                        continue
                    if type(p) is java9Parser.IdentifierContext or type(p) is java9Parser.NumericTypeContext:
                        identifier1.append(p.getText())
                        continue
                    if type(p) is java9Parser.DimsContext:
                        dict3["attributes"]["isArray"]="true"
                        continue
                    if hasattr(p, 'children'):
                        if p.children is not None:
                            for node in p.children:
                                # print(node.getText())
                                stack.append(node)
                dict3["attributes"]["type"]=identifier1[1]
                dict3["attributes"]["name"]=identifier1[0]
                type1=identifier1[1]
                dict3["children"].append(self.typeDictionary[type1])
                dict["children"].append(dict3)
                continue
            if hasattr(s, 'children'):
                if s.children is not None:
                    for node in s.children:
                        # print(node.getText())
                        queue.append(node)
        return dict


    # Function to check whether value is int
    def check_int(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    # Function to check whether value is float
    def check_float(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    # Function for checking Expression statements and getting their details
    def cal_Expression(self,ctx):
        queue=[ctx]
        while len(queue):
            s=queue.pop(0)
            if type(s) is java9Parser.ArrayAccess_lfno_primaryContext or type(s) is java9Parser.ArrayAccessContext:
                dict={"children":[{"attributes":{"type":"Array","value":s.children[0].getText()},"name":"Identifier"}],"name":"IndexAccess"}
                dict2=self.cal_Expression(s.children[2])
                dict["children"].append(dict2)
                return dict
            if type(s) is java9Parser.CastExpressionContext:
                dict={"attributes":{"type":s.children[1].getText(),"type_conversion":"true"},"children":[],"name":"FunctionCall"}
                dict2={"attributes":{"argumentTypes":[{"typeString":s.children[1].getText()}],"type":"type("+s.children[1].getText()+")"},"children":[],"name":"ElementaryTypeNameExpression"}
                dict2["children"].append(self.typeDictionary[s.children[1].getText()])
                dict3=self.cal_Expression(s.children[3])
                dict["children"].append(dict2)
                dict["children"].append(dict3)
                return dict
            if type(s) is java9Parser.IdentifierContext:
                a={"attributes":{},"name":"Identifier"}
                a["attributes"]["value"]=s.getText()
                return a
            if type(s) is tree.Tree.TerminalNodeImpl:
                b = {"attributes": {}, "name": "Literal"}
                # print(s.getText())
                a=s.getText()
                b["attributes"]["value"]=a
                if self.check_int(a):
                    b["attributes"]["type"]="int"
                elif self.check_float(a):
                    b["attributes"]["type"] = "float"
                else:
                    b["attributes"]["type"] = "String"
                return b
            if hasattr(s,'children') and len(s.children)==3:
                a = {"attributes": {"commonType": {"typeIdentifier": "t_int", "typeString": "int"}, "operator": "bye","type": "int"},"children":[],"name":"BinaryOperation"}
                b = self.cal_Expression(s.children[0])
                c = self.cal_Expression(s.children[2])
                a["attributes"]["operator"]=s.children[1].getText()
                a["children"].append(b)
                a["children"].append(c)
                return a
            if hasattr(s,'children') and len(s.children)==2:
                a={"attributes":{"prefix":"false","type":"int"},"children":[],"name":"UnaryOperation"}
                if type(s) is java9Parser.PostfixExpressionContext or type(s) is java9Parser.PostIncrementExpressionContext or type(s) is java9Parser.PostDecrementExpressionContext:
                    a["attributes"]["operator"]=s.children[1].getText()
                    b=self.cal_Expression(s.children[0])
                    a["children"].append(b)
                    pass
                else:
                    a["attributes"]["operator"]=s.children[0].getText()
                    b=self.cal_Expression(s.children[1])
                    a["children"].append(b)
                return a
            # print(type(s))
            # if type(s) is java9Parser.LiteralContext:
            #     print(type(s.children[0]))
            if hasattr(s, 'children'):
                if s.children is not None:
                    for node in s.children:
                        # print(node.getText())
                        queue.append(node)


    # Function for checking variable declaration statements and getting their details
    def fun_variable_declaration(self,ctx:java9Parser.LocalVariableDeclarationContext):
        queue=[ctx]
        a={"children":[],"name":"VariableDeclarationStatement"}
        p={"attributes":{"value":"null"},"children":[],"name":"VariableDeclaration"}
        a["children"].append(p)
        type1="int"
        sachin=[]
        while len(queue):
            s=queue.pop(0)
            if type(s) is java9Parser.VariableModifierContext:
                if s.getText()=="final":
                    a["children"][0]["attributes"]["constant"]="true"
                continue
            if type(s) is java9Parser.UnannTypeContext:
                a["children"][0]["attributes"]["type"]=s.getText()
                type1=s.getText()
                continue
            if type(s) is java9Parser.VariableDeclaratorContext:
                pandey=[]
                pandey.append(s.children[0].getText())
                if len(s.children)>1:
                    p=self.cal_Expression(s.children[2])
                    pandey.append(p)
                sachin.append(pandey)
                continue
            if hasattr(s, 'children'):
                if s.children is not None:
                    for node in s.children:
                        # print(node.getText())
                        queue.append(node)
        a["children"][0]["children"].append(self.typeDictionary[type1])
        list2=[]
        for node in sachin:
            dict2=copy.deepcopy(a)
            dict2["children"][0]["attributes"]["name"]=node[0]
            if len(node)==2:
                dict2["children"].append(node[1])
            list2.append(dict2)
        # print(list2)
        return list2

    # Function for checking block statements and getting their details
    def block_statement_constructor(self,ctx:java9Parser.BlockStatementsContext,count1):
        queue =[ctx]
        dict={}
        if count1==0:
            dict={"children":[],"name":"Block"}
        else :
            dict={"children":[]}
        while len(queue):
            s=queue.pop(0)
            # if type(s) is java9Parser.AssignmentContext:
            #     dict2={"children":[{"attributes":{"operator":"="},"children":[],"name":"Assignment"}],"name":"ExpressionStatement"}
            #     if hasattr(s, 'children'):
            #         if s.children is not None:
            #             for node in s.children:
            #                 if type(node) is java9Parser.LeftHandSideContext or type(node) is java9Parser.ExpressionContext:
            #                     dict3={"attributes":{"value":node.children[0].getText()},"name":"Identifier"}
            #                     dict2["children"].append(dict3)
            #     dict["children"].append(dict2)
            #     continue
            if type(s) is java9Parser.LocalVariableDeclarationContext:
                # print(type(s.children[1].children[0].children[2].children[0]))
                # t=s.children[1].children[0].children[2].children[0]
                # c=self.cal_Expression(t)
                # print(c)
                ans=self.fun_variable_declaration(s)
                for node in ans:
                    if node is not None:
                        dict["children"].append(node)
                continue
            if type(s) is java9Parser.AssignmentContext:
                dict2={"attributes":{"operator":"="},"children":[],"name":"Assignment"}
                a=self.cal_Expression(s.children[0])
                b=self.cal_Expression(s.children[2])
                dict2["children"].append(a)
                dict2["children"].append(b)
                dict["children"].append(dict2)
                continue
            if type(s) is java9Parser.PostDecrementExpressionContext or  type(s) is java9Parser.PostIncrementExpressionContext or type(s) is java9Parser.PreDecrementExpressionContext or type(s) is java9Parser.PreIncrementExpressionContext:
                dict2={"children":[],"name":"ExpressionStatement"}
                a=self.cal_Expression(s)
                dict2["children"].append(a)
                dict["children"].append(dict2)
                continue
            if type(s) is java9Parser.BasicForStatementContext:
                a=self.add_for_loop(s)
                dict["children"].append(a)
                continue
            if type(s) is java9Parser.IfThenElseStatementContext or type(s) is java9Parser.IfThenStatementContext:
                a=self.add_ifelse_statement(s)
                dict["children"].append(a)
                continue
            if type(s) is java9Parser.WhileStatementContext:
                a=self.add_while_statement(s)
                dict["children"].append(a)
                continue
            if type(s) is java9Parser.DoStatementContext:
                a=self.add_DoWhile_statement(s)
                dict["children"].append(a)
                continue;
            if hasattr(s, 'children'):
                if s.children is not None:
                    for node in s.children:
                        # print(node.getText())
                        queue.append(node)
        if  count1==0:
            return dict
        else:
            return dict["children"]

    # Function for checking constructors and getting their details
    def constructor_addition(self,ctx:java9Parser.ConstructorDeclarationContext):
        dict={"attributes":{"isConstructor":"true","kind":"constructor","name":"","visibility":"public","isStatic":"false"},"children":[],"name":"FunctionDefinition"}
        dict2={"attributes":{"parameters":[]},"children":[],"name":"ReturnParameterList"}
        dict["children"].append(dict2)
        queue =[ctx]
        while len(queue):
            s=queue.pop(0)
            if type(s) is java9Parser.FormalParameterListContext:
                dict3=self.add_parameterlist(s)
                dict["children"].append(dict3)
                continue
            if type(s) is java9Parser.ConstructorModifierContext:
                dict["attributes"]["visibility"]=s.children[0].getText()
                continue
            if type(s) is java9Parser.SimpleTypeNameContext:
                dict["attributes"]["name"]=s.children[0].getText()
                continue
            if type(s) is java9Parser.BlockStatementsContext:
                dict3=self.block_statement_constructor(s,0)
                dict["children"].append(dict3)
                continue
            if hasattr(s,'children'):
                if s.children is not None:
                    for node in s.children:
                        queue.append(node)
        return dict

    # Function for checking functions and getting their details
    def function_addition(self,ctx:java9Parser.MethodDeclarationContext):
        dict = {"attributes": {"isConstructor": "false", "kind": "function", "name": "", "visibility": "public","isStatic": "false"}, "children": [], "name": "FunctionDefinition"}
        dict2 = {"attributes": {"parameters": []}, "children": [], "name": "ReturnParameterList"}
        queue=[ctx]
        flag=0
        while len(queue):
            s=queue.pop(0)
            if type(s) is java9Parser.MethodModifierContext:
                if s.getText()=="protected" or s.getText()=="private":
                    dict["attributes"]["visibility"]=s.getText()
                elif s.getText()=="static":
                    dict["attributes"]["isStatic"]="true"
                continue
            if type(s) is java9Parser.IdentifierContext:
                dict["attributes"]["name"]=s.getText()
                continue
            if type(s) is java9Parser.ResultContext:
                if s.getText()=="void":
                    pass
                else:
                    type1=s.getText()
                    dict4={"attributes":{"constant":"false","name":"","value":"null","visibility":"internal"},"children":[],"name":"VariableDeclaration"}
                    dict4["attributes"]["type"]=s.getText()
                    dict4["children"].append(self.typeDictionary[type1])
                    dict2["children"].append(dict4)
                dict['children'].append(dict2)
                continue
            if type(s) is java9Parser.FormalParameterListContext:
                dict4=self.add_parameterlist(s)
                dict["children"].append(dict4)
                continue
            if type(s) is java9Parser.BlockStatementsContext:
                dict4=self.block_statement_constructor(s,0)
                dict["children"].append(dict4)
                continue
            if hasattr(s,'children'):
                if s.children is not None:
                    for node in s.children:
                        queue.append(node)
        return dict


    def appendClass(self):
        class_dictionary = {'attributes': {'baseClass':[]}, 'children': [], 'name':'ClassDefinition'}
        self.mainDictionary['children'].append(class_dictionary)

    # Function for checking variable declaration statements and getting their details
    def variable_declaration(self, ctx:java9Parser.FieldDeclarationContext):
        variable_dictionary={'attributes':{'value':"null",'constant':"false","isStatic":"false"},'children':[],'name':'variableDeclaration'}
        sachin=[]
        constant="false"
        type1=""
        visibility="public"
        isStatic="false"
        queue =[ctx]
        # print(ctx.getText())
        while len(queue):
            s=queue.pop(0)
            if type(s) is java9Parser.FieldModifierContext:
                if s.getText()=="final":
                    constant="true"
                elif s.getText()=="private":
                    visibility="private"
                elif s.getText()=="protected":
                    visibility="protected"
                elif s.getText()=="static":
                    isStatic="true"
                continue
            if type(s) is java9Parser.UnannTypeContext:
                type1=s.getText()
                continue
            if type(s) is java9Parser.VariableDeclaratorContext:
                # print(s.children[0].getText())
                # print("bye")
                if len(s.children)==3:
                    sachin.append([s.children[0].getText(),s.children[2].getText()])
                else :
                    sachin.append([s.children[0].getText()])
            if hasattr(s,'children'):
                if s.children is not None:
                    for node in s.children:
                        queue.append(node)

        variable_dictionary['attributes']['type']=type1
        variable_dictionary['attributes']['constant']=constant
        variable_dictionary['attributes']['visibility']=visibility
        variable_dictionary['attributes']['isStatic'] = isStatic
        variable_dictionary['children']=self.typeDictionary[type1]
        var_list=[]
        for val in sachin:
            a1=copy.deepcopy(variable_dictionary)
            # print(a1)
            # print(val)
            a1['attributes']['name']=val[0]
            if len(val)==2:
                a1['attributes']['value']=val[1]
            var_list.append(a1)
        # print(var_list)
        return var_list

    # Function for checking class declaration statements and getting their details
    def sachin_class(self,ctx:java9Parser.NormalClassDeclarationContext):
        class_dictionary = {'attributes': {'baseClass': []}, 'children': [], 'name': 'ClassDefinition'}
        stack = [ctx];
        a1=ctx
        flag=0;
        count_children=len(ctx.children)
        count1=0
        while len(stack):
            count1=count1+1
            # s = stack[0]
            s=stack.pop(0)
            if type(s) is java9Parser.IdentifierContext and flag==0:
                class_dictionary['attributes']['name'] = s.getText()
                flag=1
                continue
            if type(s) is java9Parser.SuperclassContext and count1<=count_children+1:
                class_dictionary['attributes']['baseClass'].append(s.children[1].getText())
                continue
            if type(s) is java9Parser.NormalClassDeclarationContext and a1!=ctx:
                a = self.sachin_class(s.children[0])
                class_dictionary['children'].append(a)
            if type(s) is java9Parser.FieldDeclarationContext:
                ans=self.variable_declaration(s)
                if ans is not None:
                    for a in ans:
                         class_dictionary['children'].append(a)
                continue
            if type(s) is java9Parser.ConstructorDeclarationContext:
                a=self.constructor_addition(ctx)
                class_dictionary['children'].append(a)
                continue
            if type(s) is java9Parser.MethodDeclarationContext:
                a=self.function_addition(s)
                class_dictionary['children'].append(a)
                continue
            if hasattr(s, 'children'):
                if s.children is not None:
                    for node in s.children:
                        # print(node.getText())
                        stack.append(node)
        # print(class_dictionary)
        return class_dictionary



    # def visitNormalClassDeclaration(self, ctx:java9Parser.NormalClassDeclarationContext):
    #     print("NormalClass")
    #     # print(ctx.getText())
    #     contextList.append(ctx)
    #     print(str(ctx.getText()))
    #     count2=count2+1;
    def visitNormalClassDeclaration(self, ctx:java9Parser.NormalClassDeclarationContext):
        # abstract=false
        # identifier=public
        # self.level=self.level+1
        # self.sachin(ctx)
        self.appendClass()

        a=ctx.children[0]
            # .getText()
        # print(str(type(a))+"   hello")
        # self.appendClass(a)
        count=len(ctx.children)
        # print(ctx.children[0])
        class_list=[]
        a1=ctx
        stack=[ctx];
        flag = 0;
        count_children = len(ctx.children)
        count1 = 0
        while len(stack):
            count1=count1+1
            # s=stack[-1]
            s=stack.pop(0)
            if type(s) is java9Parser.IdentifierContext and flag==0:
                self.mainDictionary['children'][self.child_no]['attributes']['name']=s.getText()
                flag=1
                continue
            if type(s) is java9Parser.SuperclassContext and count1<=count_children+1:
                self.mainDictionary['children'][self.child_no]['attributes']['baseClass'].append(s.children[1].getText())
            if type(s) is java9Parser.NormalClassDeclarationContext and a1!=s:
                a=self.sachin_class(s)
                self.mainDictionary['children'][self.child_no]['children'].append(a)
                continue
            if type(s) is java9Parser.FieldDeclarationContext:
                ans=self.variable_declaration(s)
                for a in ans:
                    self.mainDictionary['children'][self.child_no]['children'].append(a)
                continue
            if type(s) is java9Parser.ConstructorDeclarationContext:
                a=self.constructor_addition(ctx)
                self.mainDictionary['children'][self.child_no]['children'].append(a)
                continue
            if type(s) is java9Parser.MethodDeclarationContext:
                a=self.function_addition(s)
                self.mainDictionary['children'][self.child_no]['children'].append(a)
                continue
            if hasattr(s,'children'):
                if s.children is not None:
                    for node in s.children:
                        # print(node.getText())
                        stack.append(node)
        self.child_no=self.child_no+1


def main(argv):
    main_dict = []
    count2 = 0
    inputFile = FileStream(argv[1])
    lexer = java9Lexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = java9Parser(stream)
    tree = parser.compilationUnit()

    v = Myjava9Visitor()
    v.visit(tree)
    pprint.pprint(v.mainDictionary)
    json_object = json.dumps(v.mainDictionary, indent=3)

    with open("Output.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    main(sys.argv)
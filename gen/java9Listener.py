# Generated from /home/umang/PycharmProjects/Lab5/java9.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .java9Parser import java9Parser
else:
    from java9Parser import java9Parser

# This class defines a complete listener for a parse tree produced by java9Parser.
class java9Listener(ParseTreeListener):

    # Enter a parse tree produced by java9Parser#literal.
    def enterLiteral(self, ctx:java9Parser.LiteralContext):
        pass

    # Exit a parse tree produced by java9Parser#literal.
    def exitLiteral(self, ctx:java9Parser.LiteralContext):
        pass


    # Enter a parse tree produced by java9Parser#primitiveType.
    def enterPrimitiveType(self, ctx:java9Parser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#primitiveType.
    def exitPrimitiveType(self, ctx:java9Parser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#numericType.
    def enterNumericType(self, ctx:java9Parser.NumericTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#numericType.
    def exitNumericType(self, ctx:java9Parser.NumericTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#integralType.
    def enterIntegralType(self, ctx:java9Parser.IntegralTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#integralType.
    def exitIntegralType(self, ctx:java9Parser.IntegralTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#floatingPointType.
    def enterFloatingPointType(self, ctx:java9Parser.FloatingPointTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#floatingPointType.
    def exitFloatingPointType(self, ctx:java9Parser.FloatingPointTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#referenceType.
    def enterReferenceType(self, ctx:java9Parser.ReferenceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#referenceType.
    def exitReferenceType(self, ctx:java9Parser.ReferenceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:java9Parser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:java9Parser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#classType.
    def enterClassType(self, ctx:java9Parser.ClassTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#classType.
    def exitClassType(self, ctx:java9Parser.ClassTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#classType_lf_classOrInterfaceType.
    def enterClassType_lf_classOrInterfaceType(self, ctx:java9Parser.ClassType_lf_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#classType_lf_classOrInterfaceType.
    def exitClassType_lf_classOrInterfaceType(self, ctx:java9Parser.ClassType_lf_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#classType_lfno_classOrInterfaceType.
    def enterClassType_lfno_classOrInterfaceType(self, ctx:java9Parser.ClassType_lfno_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#classType_lfno_classOrInterfaceType.
    def exitClassType_lfno_classOrInterfaceType(self, ctx:java9Parser.ClassType_lfno_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceType.
    def enterInterfaceType(self, ctx:java9Parser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceType.
    def exitInterfaceType(self, ctx:java9Parser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceType_lf_classOrInterfaceType.
    def enterInterfaceType_lf_classOrInterfaceType(self, ctx:java9Parser.InterfaceType_lf_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceType_lf_classOrInterfaceType.
    def exitInterfaceType_lf_classOrInterfaceType(self, ctx:java9Parser.InterfaceType_lf_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceType_lfno_classOrInterfaceType.
    def enterInterfaceType_lfno_classOrInterfaceType(self, ctx:java9Parser.InterfaceType_lfno_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceType_lfno_classOrInterfaceType.
    def exitInterfaceType_lfno_classOrInterfaceType(self, ctx:java9Parser.InterfaceType_lfno_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#typeVariable.
    def enterTypeVariable(self, ctx:java9Parser.TypeVariableContext):
        pass

    # Exit a parse tree produced by java9Parser#typeVariable.
    def exitTypeVariable(self, ctx:java9Parser.TypeVariableContext):
        pass


    # Enter a parse tree produced by java9Parser#arrayType.
    def enterArrayType(self, ctx:java9Parser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#arrayType.
    def exitArrayType(self, ctx:java9Parser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#dims.
    def enterDims(self, ctx:java9Parser.DimsContext):
        pass

    # Exit a parse tree produced by java9Parser#dims.
    def exitDims(self, ctx:java9Parser.DimsContext):
        pass


    # Enter a parse tree produced by java9Parser#typeParameter.
    def enterTypeParameter(self, ctx:java9Parser.TypeParameterContext):
        pass

    # Exit a parse tree produced by java9Parser#typeParameter.
    def exitTypeParameter(self, ctx:java9Parser.TypeParameterContext):
        pass


    # Enter a parse tree produced by java9Parser#typeParameterModifier.
    def enterTypeParameterModifier(self, ctx:java9Parser.TypeParameterModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#typeParameterModifier.
    def exitTypeParameterModifier(self, ctx:java9Parser.TypeParameterModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#typeBound.
    def enterTypeBound(self, ctx:java9Parser.TypeBoundContext):
        pass

    # Exit a parse tree produced by java9Parser#typeBound.
    def exitTypeBound(self, ctx:java9Parser.TypeBoundContext):
        pass


    # Enter a parse tree produced by java9Parser#additionalBound.
    def enterAdditionalBound(self, ctx:java9Parser.AdditionalBoundContext):
        pass

    # Exit a parse tree produced by java9Parser#additionalBound.
    def exitAdditionalBound(self, ctx:java9Parser.AdditionalBoundContext):
        pass


    # Enter a parse tree produced by java9Parser#typeArguments.
    def enterTypeArguments(self, ctx:java9Parser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by java9Parser#typeArguments.
    def exitTypeArguments(self, ctx:java9Parser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by java9Parser#typeArgumentList.
    def enterTypeArgumentList(self, ctx:java9Parser.TypeArgumentListContext):
        pass

    # Exit a parse tree produced by java9Parser#typeArgumentList.
    def exitTypeArgumentList(self, ctx:java9Parser.TypeArgumentListContext):
        pass


    # Enter a parse tree produced by java9Parser#typeArgument.
    def enterTypeArgument(self, ctx:java9Parser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by java9Parser#typeArgument.
    def exitTypeArgument(self, ctx:java9Parser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by java9Parser#wildcard.
    def enterWildcard(self, ctx:java9Parser.WildcardContext):
        pass

    # Exit a parse tree produced by java9Parser#wildcard.
    def exitWildcard(self, ctx:java9Parser.WildcardContext):
        pass


    # Enter a parse tree produced by java9Parser#wildcardBounds.
    def enterWildcardBounds(self, ctx:java9Parser.WildcardBoundsContext):
        pass

    # Exit a parse tree produced by java9Parser#wildcardBounds.
    def exitWildcardBounds(self, ctx:java9Parser.WildcardBoundsContext):
        pass


    # Enter a parse tree produced by java9Parser#moduleName.
    def enterModuleName(self, ctx:java9Parser.ModuleNameContext):
        pass

    # Exit a parse tree produced by java9Parser#moduleName.
    def exitModuleName(self, ctx:java9Parser.ModuleNameContext):
        pass


    # Enter a parse tree produced by java9Parser#packageName.
    def enterPackageName(self, ctx:java9Parser.PackageNameContext):
        pass

    # Exit a parse tree produced by java9Parser#packageName.
    def exitPackageName(self, ctx:java9Parser.PackageNameContext):
        pass


    # Enter a parse tree produced by java9Parser#typeName.
    def enterTypeName(self, ctx:java9Parser.TypeNameContext):
        pass

    # Exit a parse tree produced by java9Parser#typeName.
    def exitTypeName(self, ctx:java9Parser.TypeNameContext):
        pass


    # Enter a parse tree produced by java9Parser#packageOrTypeName.
    def enterPackageOrTypeName(self, ctx:java9Parser.PackageOrTypeNameContext):
        pass

    # Exit a parse tree produced by java9Parser#packageOrTypeName.
    def exitPackageOrTypeName(self, ctx:java9Parser.PackageOrTypeNameContext):
        pass


    # Enter a parse tree produced by java9Parser#expressionName.
    def enterExpressionName(self, ctx:java9Parser.ExpressionNameContext):
        pass

    # Exit a parse tree produced by java9Parser#expressionName.
    def exitExpressionName(self, ctx:java9Parser.ExpressionNameContext):
        pass


    # Enter a parse tree produced by java9Parser#methodName.
    def enterMethodName(self, ctx:java9Parser.MethodNameContext):
        pass

    # Exit a parse tree produced by java9Parser#methodName.
    def exitMethodName(self, ctx:java9Parser.MethodNameContext):
        pass


    # Enter a parse tree produced by java9Parser#ambiguousName.
    def enterAmbiguousName(self, ctx:java9Parser.AmbiguousNameContext):
        pass

    # Exit a parse tree produced by java9Parser#ambiguousName.
    def exitAmbiguousName(self, ctx:java9Parser.AmbiguousNameContext):
        pass


    # Enter a parse tree produced by java9Parser#compilationUnit.
    def enterCompilationUnit(self, ctx:java9Parser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by java9Parser#compilationUnit.
    def exitCompilationUnit(self, ctx:java9Parser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by java9Parser#ordinaryCompilation.
    def enterOrdinaryCompilation(self, ctx:java9Parser.OrdinaryCompilationContext):
        pass

    # Exit a parse tree produced by java9Parser#ordinaryCompilation.
    def exitOrdinaryCompilation(self, ctx:java9Parser.OrdinaryCompilationContext):
        pass


    # Enter a parse tree produced by java9Parser#modularCompilation.
    def enterModularCompilation(self, ctx:java9Parser.ModularCompilationContext):
        pass

    # Exit a parse tree produced by java9Parser#modularCompilation.
    def exitModularCompilation(self, ctx:java9Parser.ModularCompilationContext):
        pass


    # Enter a parse tree produced by java9Parser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:java9Parser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:java9Parser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#packageModifier.
    def enterPackageModifier(self, ctx:java9Parser.PackageModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#packageModifier.
    def exitPackageModifier(self, ctx:java9Parser.PackageModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#importDeclaration.
    def enterImportDeclaration(self, ctx:java9Parser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#importDeclaration.
    def exitImportDeclaration(self, ctx:java9Parser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#singleTypeImportDeclaration.
    def enterSingleTypeImportDeclaration(self, ctx:java9Parser.SingleTypeImportDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#singleTypeImportDeclaration.
    def exitSingleTypeImportDeclaration(self, ctx:java9Parser.SingleTypeImportDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#typeImportOnDemandDeclaration.
    def enterTypeImportOnDemandDeclaration(self, ctx:java9Parser.TypeImportOnDemandDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#typeImportOnDemandDeclaration.
    def exitTypeImportOnDemandDeclaration(self, ctx:java9Parser.TypeImportOnDemandDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#singleStaticImportDeclaration.
    def enterSingleStaticImportDeclaration(self, ctx:java9Parser.SingleStaticImportDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#singleStaticImportDeclaration.
    def exitSingleStaticImportDeclaration(self, ctx:java9Parser.SingleStaticImportDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#staticImportOnDemandDeclaration.
    def enterStaticImportOnDemandDeclaration(self, ctx:java9Parser.StaticImportOnDemandDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#staticImportOnDemandDeclaration.
    def exitStaticImportOnDemandDeclaration(self, ctx:java9Parser.StaticImportOnDemandDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:java9Parser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:java9Parser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#moduleDeclaration.
    def enterModuleDeclaration(self, ctx:java9Parser.ModuleDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#moduleDeclaration.
    def exitModuleDeclaration(self, ctx:java9Parser.ModuleDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#moduleDirective.
    def enterModuleDirective(self, ctx:java9Parser.ModuleDirectiveContext):
        pass

    # Exit a parse tree produced by java9Parser#moduleDirective.
    def exitModuleDirective(self, ctx:java9Parser.ModuleDirectiveContext):
        pass


    # Enter a parse tree produced by java9Parser#requiresModifier.
    def enterRequiresModifier(self, ctx:java9Parser.RequiresModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#requiresModifier.
    def exitRequiresModifier(self, ctx:java9Parser.RequiresModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#classDeclaration.
    def enterClassDeclaration(self, ctx:java9Parser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#classDeclaration.
    def exitClassDeclaration(self, ctx:java9Parser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#normalClassDeclaration.
    def enterNormalClassDeclaration(self, ctx:java9Parser.NormalClassDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#normalClassDeclaration.
    def exitNormalClassDeclaration(self, ctx:java9Parser.NormalClassDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#classModifier.
    def enterClassModifier(self, ctx:java9Parser.ClassModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#classModifier.
    def exitClassModifier(self, ctx:java9Parser.ClassModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#typeParameters.
    def enterTypeParameters(self, ctx:java9Parser.TypeParametersContext):
        pass

    # Exit a parse tree produced by java9Parser#typeParameters.
    def exitTypeParameters(self, ctx:java9Parser.TypeParametersContext):
        pass


    # Enter a parse tree produced by java9Parser#typeParameterList.
    def enterTypeParameterList(self, ctx:java9Parser.TypeParameterListContext):
        pass

    # Exit a parse tree produced by java9Parser#typeParameterList.
    def exitTypeParameterList(self, ctx:java9Parser.TypeParameterListContext):
        pass


    # Enter a parse tree produced by java9Parser#superclass.
    def enterSuperclass(self, ctx:java9Parser.SuperclassContext):
        pass

    # Exit a parse tree produced by java9Parser#superclass.
    def exitSuperclass(self, ctx:java9Parser.SuperclassContext):
        pass


    # Enter a parse tree produced by java9Parser#superinterfaces.
    def enterSuperinterfaces(self, ctx:java9Parser.SuperinterfacesContext):
        pass

    # Exit a parse tree produced by java9Parser#superinterfaces.
    def exitSuperinterfaces(self, ctx:java9Parser.SuperinterfacesContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceTypeList.
    def enterInterfaceTypeList(self, ctx:java9Parser.InterfaceTypeListContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceTypeList.
    def exitInterfaceTypeList(self, ctx:java9Parser.InterfaceTypeListContext):
        pass


    # Enter a parse tree produced by java9Parser#classBody.
    def enterClassBody(self, ctx:java9Parser.ClassBodyContext):
        pass

    # Exit a parse tree produced by java9Parser#classBody.
    def exitClassBody(self, ctx:java9Parser.ClassBodyContext):
        pass


    # Enter a parse tree produced by java9Parser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:java9Parser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:java9Parser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#classMemberDeclaration.
    def enterClassMemberDeclaration(self, ctx:java9Parser.ClassMemberDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#classMemberDeclaration.
    def exitClassMemberDeclaration(self, ctx:java9Parser.ClassMemberDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:java9Parser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:java9Parser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#fieldModifier.
    def enterFieldModifier(self, ctx:java9Parser.FieldModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#fieldModifier.
    def exitFieldModifier(self, ctx:java9Parser.FieldModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#variableDeclaratorList.
    def enterVariableDeclaratorList(self, ctx:java9Parser.VariableDeclaratorListContext):
        pass

    # Exit a parse tree produced by java9Parser#variableDeclaratorList.
    def exitVariableDeclaratorList(self, ctx:java9Parser.VariableDeclaratorListContext):
        pass


    # Enter a parse tree produced by java9Parser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:java9Parser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by java9Parser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:java9Parser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by java9Parser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:java9Parser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by java9Parser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:java9Parser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by java9Parser#variableInitializer.
    def enterVariableInitializer(self, ctx:java9Parser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by java9Parser#variableInitializer.
    def exitVariableInitializer(self, ctx:java9Parser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by java9Parser#unannType.
    def enterUnannType(self, ctx:java9Parser.UnannTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannType.
    def exitUnannType(self, ctx:java9Parser.UnannTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannPrimitiveType.
    def enterUnannPrimitiveType(self, ctx:java9Parser.UnannPrimitiveTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannPrimitiveType.
    def exitUnannPrimitiveType(self, ctx:java9Parser.UnannPrimitiveTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannReferenceType.
    def enterUnannReferenceType(self, ctx:java9Parser.UnannReferenceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannReferenceType.
    def exitUnannReferenceType(self, ctx:java9Parser.UnannReferenceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannClassOrInterfaceType.
    def enterUnannClassOrInterfaceType(self, ctx:java9Parser.UnannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannClassOrInterfaceType.
    def exitUnannClassOrInterfaceType(self, ctx:java9Parser.UnannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannClassType.
    def enterUnannClassType(self, ctx:java9Parser.UnannClassTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannClassType.
    def exitUnannClassType(self, ctx:java9Parser.UnannClassTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannClassType_lf_unannClassOrInterfaceType.
    def enterUnannClassType_lf_unannClassOrInterfaceType(self, ctx:java9Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannClassType_lf_unannClassOrInterfaceType.
    def exitUnannClassType_lf_unannClassOrInterfaceType(self, ctx:java9Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannClassType_lfno_unannClassOrInterfaceType.
    def enterUnannClassType_lfno_unannClassOrInterfaceType(self, ctx:java9Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannClassType_lfno_unannClassOrInterfaceType.
    def exitUnannClassType_lfno_unannClassOrInterfaceType(self, ctx:java9Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannInterfaceType.
    def enterUnannInterfaceType(self, ctx:java9Parser.UnannInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannInterfaceType.
    def exitUnannInterfaceType(self, ctx:java9Parser.UnannInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannInterfaceType_lf_unannClassOrInterfaceType.
    def enterUnannInterfaceType_lf_unannClassOrInterfaceType(self, ctx:java9Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannInterfaceType_lf_unannClassOrInterfaceType.
    def exitUnannInterfaceType_lf_unannClassOrInterfaceType(self, ctx:java9Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannInterfaceType_lfno_unannClassOrInterfaceType.
    def enterUnannInterfaceType_lfno_unannClassOrInterfaceType(self, ctx:java9Parser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannInterfaceType_lfno_unannClassOrInterfaceType.
    def exitUnannInterfaceType_lfno_unannClassOrInterfaceType(self, ctx:java9Parser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#unannTypeVariable.
    def enterUnannTypeVariable(self, ctx:java9Parser.UnannTypeVariableContext):
        pass

    # Exit a parse tree produced by java9Parser#unannTypeVariable.
    def exitUnannTypeVariable(self, ctx:java9Parser.UnannTypeVariableContext):
        pass


    # Enter a parse tree produced by java9Parser#unannArrayType.
    def enterUnannArrayType(self, ctx:java9Parser.UnannArrayTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#unannArrayType.
    def exitUnannArrayType(self, ctx:java9Parser.UnannArrayTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:java9Parser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:java9Parser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#methodModifier.
    def enterMethodModifier(self, ctx:java9Parser.MethodModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#methodModifier.
    def exitMethodModifier(self, ctx:java9Parser.MethodModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#methodHeader.
    def enterMethodHeader(self, ctx:java9Parser.MethodHeaderContext):
        pass

    # Exit a parse tree produced by java9Parser#methodHeader.
    def exitMethodHeader(self, ctx:java9Parser.MethodHeaderContext):
        pass


    # Enter a parse tree produced by java9Parser#result.
    def enterResult(self, ctx:java9Parser.ResultContext):
        pass

    # Exit a parse tree produced by java9Parser#result.
    def exitResult(self, ctx:java9Parser.ResultContext):
        pass


    # Enter a parse tree produced by java9Parser#methodDeclarator.
    def enterMethodDeclarator(self, ctx:java9Parser.MethodDeclaratorContext):
        pass

    # Exit a parse tree produced by java9Parser#methodDeclarator.
    def exitMethodDeclarator(self, ctx:java9Parser.MethodDeclaratorContext):
        pass


    # Enter a parse tree produced by java9Parser#formalParameterList.
    def enterFormalParameterList(self, ctx:java9Parser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by java9Parser#formalParameterList.
    def exitFormalParameterList(self, ctx:java9Parser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by java9Parser#formalParameters.
    def enterFormalParameters(self, ctx:java9Parser.FormalParametersContext):
        pass

    # Exit a parse tree produced by java9Parser#formalParameters.
    def exitFormalParameters(self, ctx:java9Parser.FormalParametersContext):
        pass


    # Enter a parse tree produced by java9Parser#formalParameter.
    def enterFormalParameter(self, ctx:java9Parser.FormalParameterContext):
        pass

    # Exit a parse tree produced by java9Parser#formalParameter.
    def exitFormalParameter(self, ctx:java9Parser.FormalParameterContext):
        pass


    # Enter a parse tree produced by java9Parser#variableModifier.
    def enterVariableModifier(self, ctx:java9Parser.VariableModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#variableModifier.
    def exitVariableModifier(self, ctx:java9Parser.VariableModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:java9Parser.LastFormalParameterContext):
        pass

    # Exit a parse tree produced by java9Parser#lastFormalParameter.
    def exitLastFormalParameter(self, ctx:java9Parser.LastFormalParameterContext):
        pass


    # Enter a parse tree produced by java9Parser#receiverParameter.
    def enterReceiverParameter(self, ctx:java9Parser.ReceiverParameterContext):
        pass

    # Exit a parse tree produced by java9Parser#receiverParameter.
    def exitReceiverParameter(self, ctx:java9Parser.ReceiverParameterContext):
        pass


    # Enter a parse tree produced by java9Parser#throws_.
    def enterThrows_(self, ctx:java9Parser.Throws_Context):
        pass

    # Exit a parse tree produced by java9Parser#throws_.
    def exitThrows_(self, ctx:java9Parser.Throws_Context):
        pass


    # Enter a parse tree produced by java9Parser#exceptionTypeList.
    def enterExceptionTypeList(self, ctx:java9Parser.ExceptionTypeListContext):
        pass

    # Exit a parse tree produced by java9Parser#exceptionTypeList.
    def exitExceptionTypeList(self, ctx:java9Parser.ExceptionTypeListContext):
        pass


    # Enter a parse tree produced by java9Parser#exceptionType.
    def enterExceptionType(self, ctx:java9Parser.ExceptionTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#exceptionType.
    def exitExceptionType(self, ctx:java9Parser.ExceptionTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#methodBody.
    def enterMethodBody(self, ctx:java9Parser.MethodBodyContext):
        pass

    # Exit a parse tree produced by java9Parser#methodBody.
    def exitMethodBody(self, ctx:java9Parser.MethodBodyContext):
        pass


    # Enter a parse tree produced by java9Parser#instanceInitializer.
    def enterInstanceInitializer(self, ctx:java9Parser.InstanceInitializerContext):
        pass

    # Exit a parse tree produced by java9Parser#instanceInitializer.
    def exitInstanceInitializer(self, ctx:java9Parser.InstanceInitializerContext):
        pass


    # Enter a parse tree produced by java9Parser#staticInitializer.
    def enterStaticInitializer(self, ctx:java9Parser.StaticInitializerContext):
        pass

    # Exit a parse tree produced by java9Parser#staticInitializer.
    def exitStaticInitializer(self, ctx:java9Parser.StaticInitializerContext):
        pass


    # Enter a parse tree produced by java9Parser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:java9Parser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:java9Parser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#constructorModifier.
    def enterConstructorModifier(self, ctx:java9Parser.ConstructorModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#constructorModifier.
    def exitConstructorModifier(self, ctx:java9Parser.ConstructorModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#constructorDeclarator.
    def enterConstructorDeclarator(self, ctx:java9Parser.ConstructorDeclaratorContext):
        pass

    # Exit a parse tree produced by java9Parser#constructorDeclarator.
    def exitConstructorDeclarator(self, ctx:java9Parser.ConstructorDeclaratorContext):
        pass


    # Enter a parse tree produced by java9Parser#simpleTypeName.
    def enterSimpleTypeName(self, ctx:java9Parser.SimpleTypeNameContext):
        pass

    # Exit a parse tree produced by java9Parser#simpleTypeName.
    def exitSimpleTypeName(self, ctx:java9Parser.SimpleTypeNameContext):
        pass


    # Enter a parse tree produced by java9Parser#constructorBody.
    def enterConstructorBody(self, ctx:java9Parser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by java9Parser#constructorBody.
    def exitConstructorBody(self, ctx:java9Parser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by java9Parser#explicitConstructorInvocation.
    def enterExplicitConstructorInvocation(self, ctx:java9Parser.ExplicitConstructorInvocationContext):
        pass

    # Exit a parse tree produced by java9Parser#explicitConstructorInvocation.
    def exitExplicitConstructorInvocation(self, ctx:java9Parser.ExplicitConstructorInvocationContext):
        pass


    # Enter a parse tree produced by java9Parser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:java9Parser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:java9Parser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#enumBody.
    def enterEnumBody(self, ctx:java9Parser.EnumBodyContext):
        pass

    # Exit a parse tree produced by java9Parser#enumBody.
    def exitEnumBody(self, ctx:java9Parser.EnumBodyContext):
        pass


    # Enter a parse tree produced by java9Parser#enumConstantList.
    def enterEnumConstantList(self, ctx:java9Parser.EnumConstantListContext):
        pass

    # Exit a parse tree produced by java9Parser#enumConstantList.
    def exitEnumConstantList(self, ctx:java9Parser.EnumConstantListContext):
        pass


    # Enter a parse tree produced by java9Parser#enumConstant.
    def enterEnumConstant(self, ctx:java9Parser.EnumConstantContext):
        pass

    # Exit a parse tree produced by java9Parser#enumConstant.
    def exitEnumConstant(self, ctx:java9Parser.EnumConstantContext):
        pass


    # Enter a parse tree produced by java9Parser#enumConstantModifier.
    def enterEnumConstantModifier(self, ctx:java9Parser.EnumConstantModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#enumConstantModifier.
    def exitEnumConstantModifier(self, ctx:java9Parser.EnumConstantModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:java9Parser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by java9Parser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:java9Parser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:java9Parser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:java9Parser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#normalInterfaceDeclaration.
    def enterNormalInterfaceDeclaration(self, ctx:java9Parser.NormalInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#normalInterfaceDeclaration.
    def exitNormalInterfaceDeclaration(self, ctx:java9Parser.NormalInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceModifier.
    def enterInterfaceModifier(self, ctx:java9Parser.InterfaceModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceModifier.
    def exitInterfaceModifier(self, ctx:java9Parser.InterfaceModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#extendsInterfaces.
    def enterExtendsInterfaces(self, ctx:java9Parser.ExtendsInterfacesContext):
        pass

    # Exit a parse tree produced by java9Parser#extendsInterfaces.
    def exitExtendsInterfaces(self, ctx:java9Parser.ExtendsInterfacesContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceBody.
    def enterInterfaceBody(self, ctx:java9Parser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceBody.
    def exitInterfaceBody(self, ctx:java9Parser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:java9Parser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:java9Parser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:java9Parser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:java9Parser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#constantModifier.
    def enterConstantModifier(self, ctx:java9Parser.ConstantModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#constantModifier.
    def exitConstantModifier(self, ctx:java9Parser.ConstantModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:java9Parser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:java9Parser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#interfaceMethodModifier.
    def enterInterfaceMethodModifier(self, ctx:java9Parser.InterfaceMethodModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#interfaceMethodModifier.
    def exitInterfaceMethodModifier(self, ctx:java9Parser.InterfaceMethodModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:java9Parser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:java9Parser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:java9Parser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by java9Parser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:java9Parser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by java9Parser#annotationTypeMemberDeclaration.
    def enterAnnotationTypeMemberDeclaration(self, ctx:java9Parser.AnnotationTypeMemberDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#annotationTypeMemberDeclaration.
    def exitAnnotationTypeMemberDeclaration(self, ctx:java9Parser.AnnotationTypeMemberDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:java9Parser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:java9Parser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#annotationTypeElementModifier.
    def enterAnnotationTypeElementModifier(self, ctx:java9Parser.AnnotationTypeElementModifierContext):
        pass

    # Exit a parse tree produced by java9Parser#annotationTypeElementModifier.
    def exitAnnotationTypeElementModifier(self, ctx:java9Parser.AnnotationTypeElementModifierContext):
        pass


    # Enter a parse tree produced by java9Parser#defaultValue.
    def enterDefaultValue(self, ctx:java9Parser.DefaultValueContext):
        pass

    # Exit a parse tree produced by java9Parser#defaultValue.
    def exitDefaultValue(self, ctx:java9Parser.DefaultValueContext):
        pass


    # Enter a parse tree produced by java9Parser#annotation.
    def enterAnnotation(self, ctx:java9Parser.AnnotationContext):
        pass

    # Exit a parse tree produced by java9Parser#annotation.
    def exitAnnotation(self, ctx:java9Parser.AnnotationContext):
        pass


    # Enter a parse tree produced by java9Parser#normalAnnotation.
    def enterNormalAnnotation(self, ctx:java9Parser.NormalAnnotationContext):
        pass

    # Exit a parse tree produced by java9Parser#normalAnnotation.
    def exitNormalAnnotation(self, ctx:java9Parser.NormalAnnotationContext):
        pass


    # Enter a parse tree produced by java9Parser#elementValuePairList.
    def enterElementValuePairList(self, ctx:java9Parser.ElementValuePairListContext):
        pass

    # Exit a parse tree produced by java9Parser#elementValuePairList.
    def exitElementValuePairList(self, ctx:java9Parser.ElementValuePairListContext):
        pass


    # Enter a parse tree produced by java9Parser#elementValuePair.
    def enterElementValuePair(self, ctx:java9Parser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by java9Parser#elementValuePair.
    def exitElementValuePair(self, ctx:java9Parser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by java9Parser#elementValue.
    def enterElementValue(self, ctx:java9Parser.ElementValueContext):
        pass

    # Exit a parse tree produced by java9Parser#elementValue.
    def exitElementValue(self, ctx:java9Parser.ElementValueContext):
        pass


    # Enter a parse tree produced by java9Parser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:java9Parser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by java9Parser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:java9Parser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by java9Parser#elementValueList.
    def enterElementValueList(self, ctx:java9Parser.ElementValueListContext):
        pass

    # Exit a parse tree produced by java9Parser#elementValueList.
    def exitElementValueList(self, ctx:java9Parser.ElementValueListContext):
        pass


    # Enter a parse tree produced by java9Parser#markerAnnotation.
    def enterMarkerAnnotation(self, ctx:java9Parser.MarkerAnnotationContext):
        pass

    # Exit a parse tree produced by java9Parser#markerAnnotation.
    def exitMarkerAnnotation(self, ctx:java9Parser.MarkerAnnotationContext):
        pass


    # Enter a parse tree produced by java9Parser#singleElementAnnotation.
    def enterSingleElementAnnotation(self, ctx:java9Parser.SingleElementAnnotationContext):
        pass

    # Exit a parse tree produced by java9Parser#singleElementAnnotation.
    def exitSingleElementAnnotation(self, ctx:java9Parser.SingleElementAnnotationContext):
        pass


    # Enter a parse tree produced by java9Parser#arrayInitializer.
    def enterArrayInitializer(self, ctx:java9Parser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by java9Parser#arrayInitializer.
    def exitArrayInitializer(self, ctx:java9Parser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by java9Parser#variableInitializerList.
    def enterVariableInitializerList(self, ctx:java9Parser.VariableInitializerListContext):
        pass

    # Exit a parse tree produced by java9Parser#variableInitializerList.
    def exitVariableInitializerList(self, ctx:java9Parser.VariableInitializerListContext):
        pass


    # Enter a parse tree produced by java9Parser#block.
    def enterBlock(self, ctx:java9Parser.BlockContext):
        pass

    # Exit a parse tree produced by java9Parser#block.
    def exitBlock(self, ctx:java9Parser.BlockContext):
        pass


    # Enter a parse tree produced by java9Parser#blockStatements.
    def enterBlockStatements(self, ctx:java9Parser.BlockStatementsContext):
        pass

    # Exit a parse tree produced by java9Parser#blockStatements.
    def exitBlockStatements(self, ctx:java9Parser.BlockStatementsContext):
        pass


    # Enter a parse tree produced by java9Parser#blockStatement.
    def enterBlockStatement(self, ctx:java9Parser.BlockStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#blockStatement.
    def exitBlockStatement(self, ctx:java9Parser.BlockStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:java9Parser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:java9Parser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:java9Parser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by java9Parser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:java9Parser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by java9Parser#statement.
    def enterStatement(self, ctx:java9Parser.StatementContext):
        pass

    # Exit a parse tree produced by java9Parser#statement.
    def exitStatement(self, ctx:java9Parser.StatementContext):
        pass


    # Enter a parse tree produced by java9Parser#statementNoShortIf.
    def enterStatementNoShortIf(self, ctx:java9Parser.StatementNoShortIfContext):
        pass

    # Exit a parse tree produced by java9Parser#statementNoShortIf.
    def exitStatementNoShortIf(self, ctx:java9Parser.StatementNoShortIfContext):
        pass


    # Enter a parse tree produced by java9Parser#statementWithoutTrailingSubstatement.
    def enterStatementWithoutTrailingSubstatement(self, ctx:java9Parser.StatementWithoutTrailingSubstatementContext):
        pass

    # Exit a parse tree produced by java9Parser#statementWithoutTrailingSubstatement.
    def exitStatementWithoutTrailingSubstatement(self, ctx:java9Parser.StatementWithoutTrailingSubstatementContext):
        pass


    # Enter a parse tree produced by java9Parser#emptyStatement.
    def enterEmptyStatement(self, ctx:java9Parser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#emptyStatement.
    def exitEmptyStatement(self, ctx:java9Parser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#labeledStatement.
    def enterLabeledStatement(self, ctx:java9Parser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#labeledStatement.
    def exitLabeledStatement(self, ctx:java9Parser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#labeledStatementNoShortIf.
    def enterLabeledStatementNoShortIf(self, ctx:java9Parser.LabeledStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by java9Parser#labeledStatementNoShortIf.
    def exitLabeledStatementNoShortIf(self, ctx:java9Parser.LabeledStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by java9Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:java9Parser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#expressionStatement.
    def exitExpressionStatement(self, ctx:java9Parser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#statementExpression.
    def enterStatementExpression(self, ctx:java9Parser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#statementExpression.
    def exitStatementExpression(self, ctx:java9Parser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#ifThenStatement.
    def enterIfThenStatement(self, ctx:java9Parser.IfThenStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#ifThenStatement.
    def exitIfThenStatement(self, ctx:java9Parser.IfThenStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#ifThenElseStatement.
    def enterIfThenElseStatement(self, ctx:java9Parser.IfThenElseStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#ifThenElseStatement.
    def exitIfThenElseStatement(self, ctx:java9Parser.IfThenElseStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#ifThenElseStatementNoShortIf.
    def enterIfThenElseStatementNoShortIf(self, ctx:java9Parser.IfThenElseStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by java9Parser#ifThenElseStatementNoShortIf.
    def exitIfThenElseStatementNoShortIf(self, ctx:java9Parser.IfThenElseStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by java9Parser#assertStatement.
    def enterAssertStatement(self, ctx:java9Parser.AssertStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#assertStatement.
    def exitAssertStatement(self, ctx:java9Parser.AssertStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#switchStatement.
    def enterSwitchStatement(self, ctx:java9Parser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#switchStatement.
    def exitSwitchStatement(self, ctx:java9Parser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#switchBlock.
    def enterSwitchBlock(self, ctx:java9Parser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by java9Parser#switchBlock.
    def exitSwitchBlock(self, ctx:java9Parser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by java9Parser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:java9Parser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by java9Parser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:java9Parser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by java9Parser#switchLabels.
    def enterSwitchLabels(self, ctx:java9Parser.SwitchLabelsContext):
        pass

    # Exit a parse tree produced by java9Parser#switchLabels.
    def exitSwitchLabels(self, ctx:java9Parser.SwitchLabelsContext):
        pass


    # Enter a parse tree produced by java9Parser#switchLabel.
    def enterSwitchLabel(self, ctx:java9Parser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by java9Parser#switchLabel.
    def exitSwitchLabel(self, ctx:java9Parser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by java9Parser#enumConstantName.
    def enterEnumConstantName(self, ctx:java9Parser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by java9Parser#enumConstantName.
    def exitEnumConstantName(self, ctx:java9Parser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by java9Parser#whileStatement.
    def enterWhileStatement(self, ctx:java9Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#whileStatement.
    def exitWhileStatement(self, ctx:java9Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#whileStatementNoShortIf.
    def enterWhileStatementNoShortIf(self, ctx:java9Parser.WhileStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by java9Parser#whileStatementNoShortIf.
    def exitWhileStatementNoShortIf(self, ctx:java9Parser.WhileStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by java9Parser#doStatement.
    def enterDoStatement(self, ctx:java9Parser.DoStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#doStatement.
    def exitDoStatement(self, ctx:java9Parser.DoStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#forStatement.
    def enterForStatement(self, ctx:java9Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#forStatement.
    def exitForStatement(self, ctx:java9Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#forStatementNoShortIf.
    def enterForStatementNoShortIf(self, ctx:java9Parser.ForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by java9Parser#forStatementNoShortIf.
    def exitForStatementNoShortIf(self, ctx:java9Parser.ForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by java9Parser#basicForStatement.
    def enterBasicForStatement(self, ctx:java9Parser.BasicForStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#basicForStatement.
    def exitBasicForStatement(self, ctx:java9Parser.BasicForStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#basicForStatementNoShortIf.
    def enterBasicForStatementNoShortIf(self, ctx:java9Parser.BasicForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by java9Parser#basicForStatementNoShortIf.
    def exitBasicForStatementNoShortIf(self, ctx:java9Parser.BasicForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by java9Parser#forInit.
    def enterForInit(self, ctx:java9Parser.ForInitContext):
        pass

    # Exit a parse tree produced by java9Parser#forInit.
    def exitForInit(self, ctx:java9Parser.ForInitContext):
        pass


    # Enter a parse tree produced by java9Parser#forUpdate.
    def enterForUpdate(self, ctx:java9Parser.ForUpdateContext):
        pass

    # Exit a parse tree produced by java9Parser#forUpdate.
    def exitForUpdate(self, ctx:java9Parser.ForUpdateContext):
        pass


    # Enter a parse tree produced by java9Parser#statementExpressionList.
    def enterStatementExpressionList(self, ctx:java9Parser.StatementExpressionListContext):
        pass

    # Exit a parse tree produced by java9Parser#statementExpressionList.
    def exitStatementExpressionList(self, ctx:java9Parser.StatementExpressionListContext):
        pass


    # Enter a parse tree produced by java9Parser#enhancedForStatement.
    def enterEnhancedForStatement(self, ctx:java9Parser.EnhancedForStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#enhancedForStatement.
    def exitEnhancedForStatement(self, ctx:java9Parser.EnhancedForStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#enhancedForStatementNoShortIf.
    def enterEnhancedForStatementNoShortIf(self, ctx:java9Parser.EnhancedForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by java9Parser#enhancedForStatementNoShortIf.
    def exitEnhancedForStatementNoShortIf(self, ctx:java9Parser.EnhancedForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by java9Parser#breakStatement.
    def enterBreakStatement(self, ctx:java9Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#breakStatement.
    def exitBreakStatement(self, ctx:java9Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#continueStatement.
    def enterContinueStatement(self, ctx:java9Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#continueStatement.
    def exitContinueStatement(self, ctx:java9Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#returnStatement.
    def enterReturnStatement(self, ctx:java9Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#returnStatement.
    def exitReturnStatement(self, ctx:java9Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#throwStatement.
    def enterThrowStatement(self, ctx:java9Parser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#throwStatement.
    def exitThrowStatement(self, ctx:java9Parser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#synchronizedStatement.
    def enterSynchronizedStatement(self, ctx:java9Parser.SynchronizedStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#synchronizedStatement.
    def exitSynchronizedStatement(self, ctx:java9Parser.SynchronizedStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#tryStatement.
    def enterTryStatement(self, ctx:java9Parser.TryStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#tryStatement.
    def exitTryStatement(self, ctx:java9Parser.TryStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#catches.
    def enterCatches(self, ctx:java9Parser.CatchesContext):
        pass

    # Exit a parse tree produced by java9Parser#catches.
    def exitCatches(self, ctx:java9Parser.CatchesContext):
        pass


    # Enter a parse tree produced by java9Parser#catchClause.
    def enterCatchClause(self, ctx:java9Parser.CatchClauseContext):
        pass

    # Exit a parse tree produced by java9Parser#catchClause.
    def exitCatchClause(self, ctx:java9Parser.CatchClauseContext):
        pass


    # Enter a parse tree produced by java9Parser#catchFormalParameter.
    def enterCatchFormalParameter(self, ctx:java9Parser.CatchFormalParameterContext):
        pass

    # Exit a parse tree produced by java9Parser#catchFormalParameter.
    def exitCatchFormalParameter(self, ctx:java9Parser.CatchFormalParameterContext):
        pass


    # Enter a parse tree produced by java9Parser#catchType.
    def enterCatchType(self, ctx:java9Parser.CatchTypeContext):
        pass

    # Exit a parse tree produced by java9Parser#catchType.
    def exitCatchType(self, ctx:java9Parser.CatchTypeContext):
        pass


    # Enter a parse tree produced by java9Parser#finally_.
    def enterFinally_(self, ctx:java9Parser.Finally_Context):
        pass

    # Exit a parse tree produced by java9Parser#finally_.
    def exitFinally_(self, ctx:java9Parser.Finally_Context):
        pass


    # Enter a parse tree produced by java9Parser#tryWithResourcesStatement.
    def enterTryWithResourcesStatement(self, ctx:java9Parser.TryWithResourcesStatementContext):
        pass

    # Exit a parse tree produced by java9Parser#tryWithResourcesStatement.
    def exitTryWithResourcesStatement(self, ctx:java9Parser.TryWithResourcesStatementContext):
        pass


    # Enter a parse tree produced by java9Parser#resourceSpecification.
    def enterResourceSpecification(self, ctx:java9Parser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by java9Parser#resourceSpecification.
    def exitResourceSpecification(self, ctx:java9Parser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by java9Parser#resourceList.
    def enterResourceList(self, ctx:java9Parser.ResourceListContext):
        pass

    # Exit a parse tree produced by java9Parser#resourceList.
    def exitResourceList(self, ctx:java9Parser.ResourceListContext):
        pass


    # Enter a parse tree produced by java9Parser#resource.
    def enterResource(self, ctx:java9Parser.ResourceContext):
        pass

    # Exit a parse tree produced by java9Parser#resource.
    def exitResource(self, ctx:java9Parser.ResourceContext):
        pass


    # Enter a parse tree produced by java9Parser#variableAccess.
    def enterVariableAccess(self, ctx:java9Parser.VariableAccessContext):
        pass

    # Exit a parse tree produced by java9Parser#variableAccess.
    def exitVariableAccess(self, ctx:java9Parser.VariableAccessContext):
        pass


    # Enter a parse tree produced by java9Parser#primary.
    def enterPrimary(self, ctx:java9Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by java9Parser#primary.
    def exitPrimary(self, ctx:java9Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray.
    def enterPrimaryNoNewArray(self, ctx:java9Parser.PrimaryNoNewArrayContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray.
    def exitPrimaryNoNewArray(self, ctx:java9Parser.PrimaryNoNewArrayContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lf_arrayAccess.
    def enterPrimaryNoNewArray_lf_arrayAccess(self, ctx:java9Parser.PrimaryNoNewArray_lf_arrayAccessContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lf_arrayAccess.
    def exitPrimaryNoNewArray_lf_arrayAccess(self, ctx:java9Parser.PrimaryNoNewArray_lf_arrayAccessContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lfno_arrayAccess.
    def enterPrimaryNoNewArray_lfno_arrayAccess(self, ctx:java9Parser.PrimaryNoNewArray_lfno_arrayAccessContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lfno_arrayAccess.
    def exitPrimaryNoNewArray_lfno_arrayAccess(self, ctx:java9Parser.PrimaryNoNewArray_lfno_arrayAccessContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lf_primary.
    def enterPrimaryNoNewArray_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lf_primary.
    def exitPrimaryNoNewArray_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary.
    def enterPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary.
    def exitPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary.
    def enterPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary.
    def exitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary.
    def enterPrimaryNoNewArray_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary.
    def exitPrimaryNoNewArray_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary.
    def enterPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary.
    def exitPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary.
    def enterPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary.
    def exitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#classLiteral.
    def enterClassLiteral(self, ctx:java9Parser.ClassLiteralContext):
        pass

    # Exit a parse tree produced by java9Parser#classLiteral.
    def exitClassLiteral(self, ctx:java9Parser.ClassLiteralContext):
        pass


    # Enter a parse tree produced by java9Parser#classInstanceCreationExpression.
    def enterClassInstanceCreationExpression(self, ctx:java9Parser.ClassInstanceCreationExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#classInstanceCreationExpression.
    def exitClassInstanceCreationExpression(self, ctx:java9Parser.ClassInstanceCreationExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#classInstanceCreationExpression_lf_primary.
    def enterClassInstanceCreationExpression_lf_primary(self, ctx:java9Parser.ClassInstanceCreationExpression_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#classInstanceCreationExpression_lf_primary.
    def exitClassInstanceCreationExpression_lf_primary(self, ctx:java9Parser.ClassInstanceCreationExpression_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#classInstanceCreationExpression_lfno_primary.
    def enterClassInstanceCreationExpression_lfno_primary(self, ctx:java9Parser.ClassInstanceCreationExpression_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#classInstanceCreationExpression_lfno_primary.
    def exitClassInstanceCreationExpression_lfno_primary(self, ctx:java9Parser.ClassInstanceCreationExpression_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:java9Parser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by java9Parser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:java9Parser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by java9Parser#fieldAccess.
    def enterFieldAccess(self, ctx:java9Parser.FieldAccessContext):
        pass

    # Exit a parse tree produced by java9Parser#fieldAccess.
    def exitFieldAccess(self, ctx:java9Parser.FieldAccessContext):
        pass


    # Enter a parse tree produced by java9Parser#fieldAccess_lf_primary.
    def enterFieldAccess_lf_primary(self, ctx:java9Parser.FieldAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#fieldAccess_lf_primary.
    def exitFieldAccess_lf_primary(self, ctx:java9Parser.FieldAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#fieldAccess_lfno_primary.
    def enterFieldAccess_lfno_primary(self, ctx:java9Parser.FieldAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#fieldAccess_lfno_primary.
    def exitFieldAccess_lfno_primary(self, ctx:java9Parser.FieldAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#arrayAccess.
    def enterArrayAccess(self, ctx:java9Parser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by java9Parser#arrayAccess.
    def exitArrayAccess(self, ctx:java9Parser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by java9Parser#arrayAccess_lf_primary.
    def enterArrayAccess_lf_primary(self, ctx:java9Parser.ArrayAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#arrayAccess_lf_primary.
    def exitArrayAccess_lf_primary(self, ctx:java9Parser.ArrayAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#arrayAccess_lfno_primary.
    def enterArrayAccess_lfno_primary(self, ctx:java9Parser.ArrayAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#arrayAccess_lfno_primary.
    def exitArrayAccess_lfno_primary(self, ctx:java9Parser.ArrayAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#methodInvocation.
    def enterMethodInvocation(self, ctx:java9Parser.MethodInvocationContext):
        pass

    # Exit a parse tree produced by java9Parser#methodInvocation.
    def exitMethodInvocation(self, ctx:java9Parser.MethodInvocationContext):
        pass


    # Enter a parse tree produced by java9Parser#methodInvocation_lf_primary.
    def enterMethodInvocation_lf_primary(self, ctx:java9Parser.MethodInvocation_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#methodInvocation_lf_primary.
    def exitMethodInvocation_lf_primary(self, ctx:java9Parser.MethodInvocation_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#methodInvocation_lfno_primary.
    def enterMethodInvocation_lfno_primary(self, ctx:java9Parser.MethodInvocation_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#methodInvocation_lfno_primary.
    def exitMethodInvocation_lfno_primary(self, ctx:java9Parser.MethodInvocation_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#argumentList.
    def enterArgumentList(self, ctx:java9Parser.ArgumentListContext):
        pass

    # Exit a parse tree produced by java9Parser#argumentList.
    def exitArgumentList(self, ctx:java9Parser.ArgumentListContext):
        pass


    # Enter a parse tree produced by java9Parser#methodReference.
    def enterMethodReference(self, ctx:java9Parser.MethodReferenceContext):
        pass

    # Exit a parse tree produced by java9Parser#methodReference.
    def exitMethodReference(self, ctx:java9Parser.MethodReferenceContext):
        pass


    # Enter a parse tree produced by java9Parser#methodReference_lf_primary.
    def enterMethodReference_lf_primary(self, ctx:java9Parser.MethodReference_lf_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#methodReference_lf_primary.
    def exitMethodReference_lf_primary(self, ctx:java9Parser.MethodReference_lf_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#methodReference_lfno_primary.
    def enterMethodReference_lfno_primary(self, ctx:java9Parser.MethodReference_lfno_primaryContext):
        pass

    # Exit a parse tree produced by java9Parser#methodReference_lfno_primary.
    def exitMethodReference_lfno_primary(self, ctx:java9Parser.MethodReference_lfno_primaryContext):
        pass


    # Enter a parse tree produced by java9Parser#arrayCreationExpression.
    def enterArrayCreationExpression(self, ctx:java9Parser.ArrayCreationExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#arrayCreationExpression.
    def exitArrayCreationExpression(self, ctx:java9Parser.ArrayCreationExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#dimExprs.
    def enterDimExprs(self, ctx:java9Parser.DimExprsContext):
        pass

    # Exit a parse tree produced by java9Parser#dimExprs.
    def exitDimExprs(self, ctx:java9Parser.DimExprsContext):
        pass


    # Enter a parse tree produced by java9Parser#dimExpr.
    def enterDimExpr(self, ctx:java9Parser.DimExprContext):
        pass

    # Exit a parse tree produced by java9Parser#dimExpr.
    def exitDimExpr(self, ctx:java9Parser.DimExprContext):
        pass


    # Enter a parse tree produced by java9Parser#constantExpression.
    def enterConstantExpression(self, ctx:java9Parser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#constantExpression.
    def exitConstantExpression(self, ctx:java9Parser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#expression.
    def enterExpression(self, ctx:java9Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#expression.
    def exitExpression(self, ctx:java9Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#lambdaExpression.
    def enterLambdaExpression(self, ctx:java9Parser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#lambdaExpression.
    def exitLambdaExpression(self, ctx:java9Parser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#lambdaParameters.
    def enterLambdaParameters(self, ctx:java9Parser.LambdaParametersContext):
        pass

    # Exit a parse tree produced by java9Parser#lambdaParameters.
    def exitLambdaParameters(self, ctx:java9Parser.LambdaParametersContext):
        pass


    # Enter a parse tree produced by java9Parser#inferredFormalParameterList.
    def enterInferredFormalParameterList(self, ctx:java9Parser.InferredFormalParameterListContext):
        pass

    # Exit a parse tree produced by java9Parser#inferredFormalParameterList.
    def exitInferredFormalParameterList(self, ctx:java9Parser.InferredFormalParameterListContext):
        pass


    # Enter a parse tree produced by java9Parser#lambdaBody.
    def enterLambdaBody(self, ctx:java9Parser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by java9Parser#lambdaBody.
    def exitLambdaBody(self, ctx:java9Parser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by java9Parser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:java9Parser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:java9Parser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#assignment.
    def enterAssignment(self, ctx:java9Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by java9Parser#assignment.
    def exitAssignment(self, ctx:java9Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by java9Parser#leftHandSide.
    def enterLeftHandSide(self, ctx:java9Parser.LeftHandSideContext):
        pass

    # Exit a parse tree produced by java9Parser#leftHandSide.
    def exitLeftHandSide(self, ctx:java9Parser.LeftHandSideContext):
        pass


    # Enter a parse tree produced by java9Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:java9Parser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by java9Parser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:java9Parser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by java9Parser#conditionalExpression.
    def enterConditionalExpression(self, ctx:java9Parser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#conditionalExpression.
    def exitConditionalExpression(self, ctx:java9Parser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:java9Parser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:java9Parser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:java9Parser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:java9Parser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:java9Parser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:java9Parser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:java9Parser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:java9Parser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#andExpression.
    def enterAndExpression(self, ctx:java9Parser.AndExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#andExpression.
    def exitAndExpression(self, ctx:java9Parser.AndExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#equalityExpression.
    def enterEqualityExpression(self, ctx:java9Parser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#equalityExpression.
    def exitEqualityExpression(self, ctx:java9Parser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#relationalExpression.
    def enterRelationalExpression(self, ctx:java9Parser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#relationalExpression.
    def exitRelationalExpression(self, ctx:java9Parser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#shiftExpression.
    def enterShiftExpression(self, ctx:java9Parser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#shiftExpression.
    def exitShiftExpression(self, ctx:java9Parser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#additiveExpression.
    def enterAdditiveExpression(self, ctx:java9Parser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#additiveExpression.
    def exitAdditiveExpression(self, ctx:java9Parser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:java9Parser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:java9Parser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:java9Parser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#unaryExpression.
    def exitUnaryExpression(self, ctx:java9Parser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#preIncrementExpression.
    def enterPreIncrementExpression(self, ctx:java9Parser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#preIncrementExpression.
    def exitPreIncrementExpression(self, ctx:java9Parser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#preDecrementExpression.
    def enterPreDecrementExpression(self, ctx:java9Parser.PreDecrementExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#preDecrementExpression.
    def exitPreDecrementExpression(self, ctx:java9Parser.PreDecrementExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#unaryExpressionNotPlusMinus.
    def enterUnaryExpressionNotPlusMinus(self, ctx:java9Parser.UnaryExpressionNotPlusMinusContext):
        pass

    # Exit a parse tree produced by java9Parser#unaryExpressionNotPlusMinus.
    def exitUnaryExpressionNotPlusMinus(self, ctx:java9Parser.UnaryExpressionNotPlusMinusContext):
        pass


    # Enter a parse tree produced by java9Parser#postfixExpression.
    def enterPostfixExpression(self, ctx:java9Parser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#postfixExpression.
    def exitPostfixExpression(self, ctx:java9Parser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#postIncrementExpression.
    def enterPostIncrementExpression(self, ctx:java9Parser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#postIncrementExpression.
    def exitPostIncrementExpression(self, ctx:java9Parser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#postIncrementExpression_lf_postfixExpression.
    def enterPostIncrementExpression_lf_postfixExpression(self, ctx:java9Parser.PostIncrementExpression_lf_postfixExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#postIncrementExpression_lf_postfixExpression.
    def exitPostIncrementExpression_lf_postfixExpression(self, ctx:java9Parser.PostIncrementExpression_lf_postfixExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#postDecrementExpression.
    def enterPostDecrementExpression(self, ctx:java9Parser.PostDecrementExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#postDecrementExpression.
    def exitPostDecrementExpression(self, ctx:java9Parser.PostDecrementExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#postDecrementExpression_lf_postfixExpression.
    def enterPostDecrementExpression_lf_postfixExpression(self, ctx:java9Parser.PostDecrementExpression_lf_postfixExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#postDecrementExpression_lf_postfixExpression.
    def exitPostDecrementExpression_lf_postfixExpression(self, ctx:java9Parser.PostDecrementExpression_lf_postfixExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#castExpression.
    def enterCastExpression(self, ctx:java9Parser.CastExpressionContext):
        pass

    # Exit a parse tree produced by java9Parser#castExpression.
    def exitCastExpression(self, ctx:java9Parser.CastExpressionContext):
        pass


    # Enter a parse tree produced by java9Parser#identifier.
    def enterIdentifier(self, ctx:java9Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by java9Parser#identifier.
    def exitIdentifier(self, ctx:java9Parser.IdentifierContext):
        pass



del java9Parser
# Generated from /home/umang/PycharmProjects/Lab5/java9.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .java9Parser import java9Parser
else:
    from java9Parser import java9Parser

# This class defines a complete generic visitor for a parse tree produced by java9Parser.

class java9Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by java9Parser#literal.
    def visitLiteral(self, ctx:java9Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primitiveType.
    def visitPrimitiveType(self, ctx:java9Parser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#numericType.
    def visitNumericType(self, ctx:java9Parser.NumericTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#integralType.
    def visitIntegralType(self, ctx:java9Parser.IntegralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#floatingPointType.
    def visitFloatingPointType(self, ctx:java9Parser.FloatingPointTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#referenceType.
    def visitReferenceType(self, ctx:java9Parser.ReferenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx:java9Parser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classType.
    def visitClassType(self, ctx:java9Parser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classType_lf_classOrInterfaceType.
    def visitClassType_lf_classOrInterfaceType(self, ctx:java9Parser.ClassType_lf_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classType_lfno_classOrInterfaceType.
    def visitClassType_lfno_classOrInterfaceType(self, ctx:java9Parser.ClassType_lfno_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceType.
    def visitInterfaceType(self, ctx:java9Parser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceType_lf_classOrInterfaceType.
    def visitInterfaceType_lf_classOrInterfaceType(self, ctx:java9Parser.InterfaceType_lf_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceType_lfno_classOrInterfaceType.
    def visitInterfaceType_lfno_classOrInterfaceType(self, ctx:java9Parser.InterfaceType_lfno_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeVariable.
    def visitTypeVariable(self, ctx:java9Parser.TypeVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#arrayType.
    def visitArrayType(self, ctx:java9Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#dims.
    def visitDims(self, ctx:java9Parser.DimsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeParameter.
    def visitTypeParameter(self, ctx:java9Parser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeParameterModifier.
    def visitTypeParameterModifier(self, ctx:java9Parser.TypeParameterModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeBound.
    def visitTypeBound(self, ctx:java9Parser.TypeBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#additionalBound.
    def visitAdditionalBound(self, ctx:java9Parser.AdditionalBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeArguments.
    def visitTypeArguments(self, ctx:java9Parser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeArgumentList.
    def visitTypeArgumentList(self, ctx:java9Parser.TypeArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeArgument.
    def visitTypeArgument(self, ctx:java9Parser.TypeArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#wildcard.
    def visitWildcard(self, ctx:java9Parser.WildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#wildcardBounds.
    def visitWildcardBounds(self, ctx:java9Parser.WildcardBoundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#moduleName.
    def visitModuleName(self, ctx:java9Parser.ModuleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#packageName.
    def visitPackageName(self, ctx:java9Parser.PackageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeName.
    def visitTypeName(self, ctx:java9Parser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#packageOrTypeName.
    def visitPackageOrTypeName(self, ctx:java9Parser.PackageOrTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#expressionName.
    def visitExpressionName(self, ctx:java9Parser.ExpressionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodName.
    def visitMethodName(self, ctx:java9Parser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#ambiguousName.
    def visitAmbiguousName(self, ctx:java9Parser.AmbiguousNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#compilationUnit.
    def visitCompilationUnit(self, ctx:java9Parser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#ordinaryCompilation.
    def visitOrdinaryCompilation(self, ctx:java9Parser.OrdinaryCompilationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#modularCompilation.
    def visitModularCompilation(self, ctx:java9Parser.ModularCompilationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:java9Parser.PackageDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#packageModifier.
    def visitPackageModifier(self, ctx:java9Parser.PackageModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#importDeclaration.
    def visitImportDeclaration(self, ctx:java9Parser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#singleTypeImportDeclaration.
    def visitSingleTypeImportDeclaration(self, ctx:java9Parser.SingleTypeImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeImportOnDemandDeclaration.
    def visitTypeImportOnDemandDeclaration(self, ctx:java9Parser.TypeImportOnDemandDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#singleStaticImportDeclaration.
    def visitSingleStaticImportDeclaration(self, ctx:java9Parser.SingleStaticImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#staticImportOnDemandDeclaration.
    def visitStaticImportOnDemandDeclaration(self, ctx:java9Parser.StaticImportOnDemandDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:java9Parser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#moduleDeclaration.
    def visitModuleDeclaration(self, ctx:java9Parser.ModuleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#moduleDirective.
    def visitModuleDirective(self, ctx:java9Parser.ModuleDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#requiresModifier.
    def visitRequiresModifier(self, ctx:java9Parser.RequiresModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classDeclaration.
    def visitClassDeclaration(self, ctx:java9Parser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#normalClassDeclaration.
    def visitNormalClassDeclaration(self, ctx:java9Parser.NormalClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classModifier.
    def visitClassModifier(self, ctx:java9Parser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeParameters.
    def visitTypeParameters(self, ctx:java9Parser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeParameterList.
    def visitTypeParameterList(self, ctx:java9Parser.TypeParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#superclass.
    def visitSuperclass(self, ctx:java9Parser.SuperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#superinterfaces.
    def visitSuperinterfaces(self, ctx:java9Parser.SuperinterfacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceTypeList.
    def visitInterfaceTypeList(self, ctx:java9Parser.InterfaceTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classBody.
    def visitClassBody(self, ctx:java9Parser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:java9Parser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classMemberDeclaration.
    def visitClassMemberDeclaration(self, ctx:java9Parser.ClassMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:java9Parser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#fieldModifier.
    def visitFieldModifier(self, ctx:java9Parser.FieldModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#variableDeclaratorList.
    def visitVariableDeclaratorList(self, ctx:java9Parser.VariableDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:java9Parser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:java9Parser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#variableInitializer.
    def visitVariableInitializer(self, ctx:java9Parser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannType.
    def visitUnannType(self, ctx:java9Parser.UnannTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannPrimitiveType.
    def visitUnannPrimitiveType(self, ctx:java9Parser.UnannPrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannReferenceType.
    def visitUnannReferenceType(self, ctx:java9Parser.UnannReferenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannClassOrInterfaceType.
    def visitUnannClassOrInterfaceType(self, ctx:java9Parser.UnannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannClassType.
    def visitUnannClassType(self, ctx:java9Parser.UnannClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannClassType_lf_unannClassOrInterfaceType.
    def visitUnannClassType_lf_unannClassOrInterfaceType(self, ctx:java9Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannClassType_lfno_unannClassOrInterfaceType.
    def visitUnannClassType_lfno_unannClassOrInterfaceType(self, ctx:java9Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannInterfaceType.
    def visitUnannInterfaceType(self, ctx:java9Parser.UnannInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannInterfaceType_lf_unannClassOrInterfaceType.
    def visitUnannInterfaceType_lf_unannClassOrInterfaceType(self, ctx:java9Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannInterfaceType_lfno_unannClassOrInterfaceType.
    def visitUnannInterfaceType_lfno_unannClassOrInterfaceType(self, ctx:java9Parser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannTypeVariable.
    def visitUnannTypeVariable(self, ctx:java9Parser.UnannTypeVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unannArrayType.
    def visitUnannArrayType(self, ctx:java9Parser.UnannArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:java9Parser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodModifier.
    def visitMethodModifier(self, ctx:java9Parser.MethodModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodHeader.
    def visitMethodHeader(self, ctx:java9Parser.MethodHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#result.
    def visitResult(self, ctx:java9Parser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodDeclarator.
    def visitMethodDeclarator(self, ctx:java9Parser.MethodDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#formalParameterList.
    def visitFormalParameterList(self, ctx:java9Parser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#formalParameters.
    def visitFormalParameters(self, ctx:java9Parser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#formalParameter.
    def visitFormalParameter(self, ctx:java9Parser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#variableModifier.
    def visitVariableModifier(self, ctx:java9Parser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#lastFormalParameter.
    def visitLastFormalParameter(self, ctx:java9Parser.LastFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#receiverParameter.
    def visitReceiverParameter(self, ctx:java9Parser.ReceiverParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#throws_.
    def visitThrows_(self, ctx:java9Parser.Throws_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#exceptionTypeList.
    def visitExceptionTypeList(self, ctx:java9Parser.ExceptionTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#exceptionType.
    def visitExceptionType(self, ctx:java9Parser.ExceptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodBody.
    def visitMethodBody(self, ctx:java9Parser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#instanceInitializer.
    def visitInstanceInitializer(self, ctx:java9Parser.InstanceInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#staticInitializer.
    def visitStaticInitializer(self, ctx:java9Parser.StaticInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:java9Parser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#constructorModifier.
    def visitConstructorModifier(self, ctx:java9Parser.ConstructorModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#constructorDeclarator.
    def visitConstructorDeclarator(self, ctx:java9Parser.ConstructorDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#simpleTypeName.
    def visitSimpleTypeName(self, ctx:java9Parser.SimpleTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#constructorBody.
    def visitConstructorBody(self, ctx:java9Parser.ConstructorBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#explicitConstructorInvocation.
    def visitExplicitConstructorInvocation(self, ctx:java9Parser.ExplicitConstructorInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:java9Parser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enumBody.
    def visitEnumBody(self, ctx:java9Parser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enumConstantList.
    def visitEnumConstantList(self, ctx:java9Parser.EnumConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enumConstant.
    def visitEnumConstant(self, ctx:java9Parser.EnumConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enumConstantModifier.
    def visitEnumConstantModifier(self, ctx:java9Parser.EnumConstantModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enumBodyDeclarations.
    def visitEnumBodyDeclarations(self, ctx:java9Parser.EnumBodyDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:java9Parser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#normalInterfaceDeclaration.
    def visitNormalInterfaceDeclaration(self, ctx:java9Parser.NormalInterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceModifier.
    def visitInterfaceModifier(self, ctx:java9Parser.InterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#extendsInterfaces.
    def visitExtendsInterfaces(self, ctx:java9Parser.ExtendsInterfacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceBody.
    def visitInterfaceBody(self, ctx:java9Parser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceMemberDeclaration.
    def visitInterfaceMemberDeclaration(self, ctx:java9Parser.InterfaceMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:java9Parser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#constantModifier.
    def visitConstantModifier(self, ctx:java9Parser.ConstantModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceMethodDeclaration.
    def visitInterfaceMethodDeclaration(self, ctx:java9Parser.InterfaceMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#interfaceMethodModifier.
    def visitInterfaceMethodModifier(self, ctx:java9Parser.InterfaceMethodModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#annotationTypeDeclaration.
    def visitAnnotationTypeDeclaration(self, ctx:java9Parser.AnnotationTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#annotationTypeBody.
    def visitAnnotationTypeBody(self, ctx:java9Parser.AnnotationTypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#annotationTypeMemberDeclaration.
    def visitAnnotationTypeMemberDeclaration(self, ctx:java9Parser.AnnotationTypeMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#annotationTypeElementDeclaration.
    def visitAnnotationTypeElementDeclaration(self, ctx:java9Parser.AnnotationTypeElementDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#annotationTypeElementModifier.
    def visitAnnotationTypeElementModifier(self, ctx:java9Parser.AnnotationTypeElementModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#defaultValue.
    def visitDefaultValue(self, ctx:java9Parser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#annotation.
    def visitAnnotation(self, ctx:java9Parser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#normalAnnotation.
    def visitNormalAnnotation(self, ctx:java9Parser.NormalAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#elementValuePairList.
    def visitElementValuePairList(self, ctx:java9Parser.ElementValuePairListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#elementValuePair.
    def visitElementValuePair(self, ctx:java9Parser.ElementValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#elementValue.
    def visitElementValue(self, ctx:java9Parser.ElementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx:java9Parser.ElementValueArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#elementValueList.
    def visitElementValueList(self, ctx:java9Parser.ElementValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#markerAnnotation.
    def visitMarkerAnnotation(self, ctx:java9Parser.MarkerAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#singleElementAnnotation.
    def visitSingleElementAnnotation(self, ctx:java9Parser.SingleElementAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#arrayInitializer.
    def visitArrayInitializer(self, ctx:java9Parser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#variableInitializerList.
    def visitVariableInitializerList(self, ctx:java9Parser.VariableInitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#block.
    def visitBlock(self, ctx:java9Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#blockStatements.
    def visitBlockStatements(self, ctx:java9Parser.BlockStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#blockStatement.
    def visitBlockStatement(self, ctx:java9Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#localVariableDeclarationStatement.
    def visitLocalVariableDeclarationStatement(self, ctx:java9Parser.LocalVariableDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:java9Parser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#statement.
    def visitStatement(self, ctx:java9Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#statementNoShortIf.
    def visitStatementNoShortIf(self, ctx:java9Parser.StatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#statementWithoutTrailingSubstatement.
    def visitStatementWithoutTrailingSubstatement(self, ctx:java9Parser.StatementWithoutTrailingSubstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#emptyStatement.
    def visitEmptyStatement(self, ctx:java9Parser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#labeledStatement.
    def visitLabeledStatement(self, ctx:java9Parser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#labeledStatementNoShortIf.
    def visitLabeledStatementNoShortIf(self, ctx:java9Parser.LabeledStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#expressionStatement.
    def visitExpressionStatement(self, ctx:java9Parser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#statementExpression.
    def visitStatementExpression(self, ctx:java9Parser.StatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#ifThenStatement.
    def visitIfThenStatement(self, ctx:java9Parser.IfThenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#ifThenElseStatement.
    def visitIfThenElseStatement(self, ctx:java9Parser.IfThenElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#ifThenElseStatementNoShortIf.
    def visitIfThenElseStatementNoShortIf(self, ctx:java9Parser.IfThenElseStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#assertStatement.
    def visitAssertStatement(self, ctx:java9Parser.AssertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#switchStatement.
    def visitSwitchStatement(self, ctx:java9Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#switchBlock.
    def visitSwitchBlock(self, ctx:java9Parser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:java9Parser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#switchLabels.
    def visitSwitchLabels(self, ctx:java9Parser.SwitchLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#switchLabel.
    def visitSwitchLabel(self, ctx:java9Parser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enumConstantName.
    def visitEnumConstantName(self, ctx:java9Parser.EnumConstantNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#whileStatement.
    def visitWhileStatement(self, ctx:java9Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#whileStatementNoShortIf.
    def visitWhileStatementNoShortIf(self, ctx:java9Parser.WhileStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#doStatement.
    def visitDoStatement(self, ctx:java9Parser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#forStatement.
    def visitForStatement(self, ctx:java9Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#forStatementNoShortIf.
    def visitForStatementNoShortIf(self, ctx:java9Parser.ForStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#basicForStatement.
    def visitBasicForStatement(self, ctx:java9Parser.BasicForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#basicForStatementNoShortIf.
    def visitBasicForStatementNoShortIf(self, ctx:java9Parser.BasicForStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#forInit.
    def visitForInit(self, ctx:java9Parser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#forUpdate.
    def visitForUpdate(self, ctx:java9Parser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#statementExpressionList.
    def visitStatementExpressionList(self, ctx:java9Parser.StatementExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enhancedForStatement.
    def visitEnhancedForStatement(self, ctx:java9Parser.EnhancedForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#enhancedForStatementNoShortIf.
    def visitEnhancedForStatementNoShortIf(self, ctx:java9Parser.EnhancedForStatementNoShortIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#breakStatement.
    def visitBreakStatement(self, ctx:java9Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#continueStatement.
    def visitContinueStatement(self, ctx:java9Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#returnStatement.
    def visitReturnStatement(self, ctx:java9Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#throwStatement.
    def visitThrowStatement(self, ctx:java9Parser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#synchronizedStatement.
    def visitSynchronizedStatement(self, ctx:java9Parser.SynchronizedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#tryStatement.
    def visitTryStatement(self, ctx:java9Parser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#catches.
    def visitCatches(self, ctx:java9Parser.CatchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#catchClause.
    def visitCatchClause(self, ctx:java9Parser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#catchFormalParameter.
    def visitCatchFormalParameter(self, ctx:java9Parser.CatchFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#catchType.
    def visitCatchType(self, ctx:java9Parser.CatchTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#finally_.
    def visitFinally_(self, ctx:java9Parser.Finally_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#tryWithResourcesStatement.
    def visitTryWithResourcesStatement(self, ctx:java9Parser.TryWithResourcesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#resourceSpecification.
    def visitResourceSpecification(self, ctx:java9Parser.ResourceSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#resourceList.
    def visitResourceList(self, ctx:java9Parser.ResourceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#resource.
    def visitResource(self, ctx:java9Parser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#variableAccess.
    def visitVariableAccess(self, ctx:java9Parser.VariableAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primary.
    def visitPrimary(self, ctx:java9Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray.
    def visitPrimaryNoNewArray(self, ctx:java9Parser.PrimaryNoNewArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lf_arrayAccess.
    def visitPrimaryNoNewArray_lf_arrayAccess(self, ctx:java9Parser.PrimaryNoNewArray_lf_arrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lfno_arrayAccess.
    def visitPrimaryNoNewArray_lfno_arrayAccess(self, ctx:java9Parser.PrimaryNoNewArray_lfno_arrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lf_primary.
    def visitPrimaryNoNewArray_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary.
    def visitPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary.
    def visitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self, ctx:java9Parser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary.
    def visitPrimaryNoNewArray_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary.
    def visitPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self, ctx:java9Parser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classLiteral.
    def visitClassLiteral(self, ctx:java9Parser.ClassLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classInstanceCreationExpression.
    def visitClassInstanceCreationExpression(self, ctx:java9Parser.ClassInstanceCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classInstanceCreationExpression_lf_primary.
    def visitClassInstanceCreationExpression_lf_primary(self, ctx:java9Parser.ClassInstanceCreationExpression_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#classInstanceCreationExpression_lfno_primary.
    def visitClassInstanceCreationExpression_lfno_primary(self, ctx:java9Parser.ClassInstanceCreationExpression_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#typeArgumentsOrDiamond.
    def visitTypeArgumentsOrDiamond(self, ctx:java9Parser.TypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#fieldAccess.
    def visitFieldAccess(self, ctx:java9Parser.FieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#fieldAccess_lf_primary.
    def visitFieldAccess_lf_primary(self, ctx:java9Parser.FieldAccess_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#fieldAccess_lfno_primary.
    def visitFieldAccess_lfno_primary(self, ctx:java9Parser.FieldAccess_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#arrayAccess.
    def visitArrayAccess(self, ctx:java9Parser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#arrayAccess_lf_primary.
    def visitArrayAccess_lf_primary(self, ctx:java9Parser.ArrayAccess_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#arrayAccess_lfno_primary.
    def visitArrayAccess_lfno_primary(self, ctx:java9Parser.ArrayAccess_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodInvocation.
    def visitMethodInvocation(self, ctx:java9Parser.MethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodInvocation_lf_primary.
    def visitMethodInvocation_lf_primary(self, ctx:java9Parser.MethodInvocation_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodInvocation_lfno_primary.
    def visitMethodInvocation_lfno_primary(self, ctx:java9Parser.MethodInvocation_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#argumentList.
    def visitArgumentList(self, ctx:java9Parser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodReference.
    def visitMethodReference(self, ctx:java9Parser.MethodReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodReference_lf_primary.
    def visitMethodReference_lf_primary(self, ctx:java9Parser.MethodReference_lf_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#methodReference_lfno_primary.
    def visitMethodReference_lfno_primary(self, ctx:java9Parser.MethodReference_lfno_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#arrayCreationExpression.
    def visitArrayCreationExpression(self, ctx:java9Parser.ArrayCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#dimExprs.
    def visitDimExprs(self, ctx:java9Parser.DimExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#dimExpr.
    def visitDimExpr(self, ctx:java9Parser.DimExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#constantExpression.
    def visitConstantExpression(self, ctx:java9Parser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#expression.
    def visitExpression(self, ctx:java9Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#lambdaExpression.
    def visitLambdaExpression(self, ctx:java9Parser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#lambdaParameters.
    def visitLambdaParameters(self, ctx:java9Parser.LambdaParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#inferredFormalParameterList.
    def visitInferredFormalParameterList(self, ctx:java9Parser.InferredFormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#lambdaBody.
    def visitLambdaBody(self, ctx:java9Parser.LambdaBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:java9Parser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#assignment.
    def visitAssignment(self, ctx:java9Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#leftHandSide.
    def visitLeftHandSide(self, ctx:java9Parser.LeftHandSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:java9Parser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#conditionalExpression.
    def visitConditionalExpression(self, ctx:java9Parser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#conditionalOrExpression.
    def visitConditionalOrExpression(self, ctx:java9Parser.ConditionalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#conditionalAndExpression.
    def visitConditionalAndExpression(self, ctx:java9Parser.ConditionalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:java9Parser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:java9Parser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#andExpression.
    def visitAndExpression(self, ctx:java9Parser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#equalityExpression.
    def visitEqualityExpression(self, ctx:java9Parser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:java9Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#shiftExpression.
    def visitShiftExpression(self, ctx:java9Parser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:java9Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:java9Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:java9Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#preIncrementExpression.
    def visitPreIncrementExpression(self, ctx:java9Parser.PreIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#preDecrementExpression.
    def visitPreDecrementExpression(self, ctx:java9Parser.PreDecrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#unaryExpressionNotPlusMinus.
    def visitUnaryExpressionNotPlusMinus(self, ctx:java9Parser.UnaryExpressionNotPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#postfixExpression.
    def visitPostfixExpression(self, ctx:java9Parser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#postIncrementExpression.
    def visitPostIncrementExpression(self, ctx:java9Parser.PostIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#postIncrementExpression_lf_postfixExpression.
    def visitPostIncrementExpression_lf_postfixExpression(self, ctx:java9Parser.PostIncrementExpression_lf_postfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#postDecrementExpression.
    def visitPostDecrementExpression(self, ctx:java9Parser.PostDecrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#postDecrementExpression_lf_postfixExpression.
    def visitPostDecrementExpression_lf_postfixExpression(self, ctx:java9Parser.PostDecrementExpression_lf_postfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#castExpression.
    def visitCastExpression(self, ctx:java9Parser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java9Parser#identifier.
    def visitIdentifier(self, ctx:java9Parser.IdentifierContext):
        return self.visitChildren(ctx)



del java9Parser
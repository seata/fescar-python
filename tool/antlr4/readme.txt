cd tool/antlr4
java -jar antlr4-4.9.2-complete.jar -Dlanguage=Python3 *.g4 -visitor

export CLASSPATH=".:antlr4-4.9.2-complete.jar"
java org.antlr.v4.gui.TestRig
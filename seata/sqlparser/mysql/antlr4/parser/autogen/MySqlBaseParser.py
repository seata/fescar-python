# Generated from MySqlBaseParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0446")
        buf.write("\u01ff\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\5\2b\n\2\3\2\5\2e\n\2\3\2\3\2\3\3\3")
        buf.write("\3\5\3k\n\3\3\3\5\3n\n\3\3\3\7\3q\n\3\f\3\16\3t\13\3\3")
        buf.write("\3\3\3\5\3x\n\3\3\3\5\3{\n\3\3\3\5\3~\n\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\5\6\u0088\n\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u008f\n\7\3\7\5\7\u0092\n\7\3\7\5\7\u0095\n\7\3\7")
        buf.write("\5\7\u0098\n\7\3\b\3\b\5\b\u009c\n\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\b\u00a4\n\b\3\b\3\b\3\b\3\t\3\t\5\t\u00ab\n\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\7\t\u00b2\n\t\f\t\16\t\u00b5\13\t")
        buf.write("\3\t\5\t\u00b8\n\t\3\t\5\t\u00bb\n\t\3\t\5\t\u00be\n\t")
        buf.write("\3\n\3\n\5\n\u00c2\n\n\3\n\5\n\u00c5\n\n\3\n\3\n\3\n\5")
        buf.write("\n\u00ca\n\n\3\n\5\n\u00cd\n\n\3\n\3\n\5\n\u00d1\n\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00dc")
        buf.write("\n\13\f\13\16\13\u00df\13\13\3\f\3\f\5\f\u00e3\n\f\3\f")
        buf.write("\3\f\7\f\u00e7\n\f\f\f\16\f\u00ea\13\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00f2\n\r\3\r\5\r\u00f5\n\r\5\r\u00f7\n\r")
        buf.write("\3\16\3\16\5\16\u00fb\n\16\3\16\5\16\u00fe\n\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\21\5\21\u0107\n\21\3\22\3\22")
        buf.write("\3\22\5\22\u010c\n\22\5\22\u010e\n\22\3\22\3\22\3\22\5")
        buf.write("\22\u0113\n\22\5\22\u0115\n\22\3\23\3\23\3\23\5\23\u011a")
        buf.write("\n\23\3\24\3\24\3\24\7\24\u011f\n\24\f\24\16\24\u0122")
        buf.write("\13\24\3\25\3\25\3\25\5\25\u0127\n\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u012d\n\26\3\27\3\27\3\27\3\30\3\30\3\30\7\30")
        buf.write("\u0135\n\30\f\30\16\30\u0138\13\30\3\31\3\31\3\31\5\31")
        buf.write("\u013d\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u014b\n\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0151\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u015a\n\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0162")
        buf.write("\n\31\3\31\3\31\3\31\3\31\7\31\u0168\n\31\f\31\16\31\u016b")
        buf.write("\13\31\3\32\3\32\3\32\5\32\u0170\n\32\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u0176\n\33\3\33\3\33\5\33\u017a\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0193\n\34\3\35\3\35\3\35\5\35\u0198\n\35\3\36\3\36\3")
        buf.write("\36\7\36\u019d\n\36\f\36\16\36\u01a0\13\36\3\37\3\37\3")
        buf.write("\37\5\37\u01a5\n\37\3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\5!\u01b7\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u01c0\n\"\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$")
        buf.write("\u01ce\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\3,\3,\3,\3,\3,\7,\u01e3\n,\f,\16,\u01e6\13,\3-\3-\5-")
        buf.write("\u01ea\n-\3.\3.\5.\u01ee\n.\3.\5.\u01f1\n.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3/\5/\u01fb\n/\3\60\3\60\3\60\2\3\60\61\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^\2\n\4\2\u00d9\u00d9\u0293\u0293")
        buf.write("\4\2OO\u0148\u014b\24\2\32\32QQ\u0086\u0086\u00b4\u00b4")
        buf.write("\u00b6\u00b6\u00f6\u00f8\u00fa\u00fa\u0118\u0137\u013c")
        buf.write("\u013c\u0153\u0153\u01d1\u01d1\u0297\u0297\u02a5\u02ac")
        buf.write("\u02cf\u02cf\u030e\u030e\u0311\u032e\u0330\u03d4\u03d6")
        buf.write("\u043a\31\2NNZZqq\u0098\u0098\u009e\u009e\u00c6\u00c6")
        buf.write("\u010c\u010c\u0138\u0147\u015b\u01d0\u01d2\u024a\u024c")
        buf.write("\u0273\u0275\u027e\u0280\u0295\u0298\u029f\u02a4\u02a4")
        buf.write("\u02b7\u02bf\u02c4\u02c5\u02c7\u02cd\u02cf\u02d5\u0303")
        buf.write("\u0303\u032f\u032f\u03d5\u03d5\u0446\u0446\4\2gg\u00cf")
        buf.write("\u00cf\4\2,.\u043d\u043d\4\2::WW\3\2\7\t\2\u023f\2a\3")
        buf.write("\2\2\2\4r\3\2\2\2\6\177\3\2\2\2\b\u0081\3\2\2\2\n\u0087")
        buf.write("\3\2\2\2\f\u0089\3\2\2\2\16\u0099\3\2\2\2\20\u00a8\3\2")
        buf.write("\2\2\22\u00bf\3\2\2\2\24\u00d2\3\2\2\2\26\u00e2\3\2\2")
        buf.write("\2\30\u00f6\3\2\2\2\32\u00f8\3\2\2\2\34\u00ff\3\2\2\2")
        buf.write("\36\u0101\3\2\2\2 \u0103\3\2\2\2\"\u0114\3\2\2\2$\u0119")
        buf.write("\3\2\2\2&\u011b\3\2\2\2(\u0126\3\2\2\2*\u0128\3\2\2\2")
        buf.write(",\u012e\3\2\2\2.\u0131\3\2\2\2\60\u0161\3\2\2\2\62\u016f")
        buf.write("\3\2\2\2\64\u0179\3\2\2\2\66\u0192\3\2\2\28\u0194\3\2")
        buf.write("\2\2:\u0199\3\2\2\2<\u01a4\3\2\2\2>\u01a6\3\2\2\2@\u01b6")
        buf.write("\3\2\2\2B\u01bf\3\2\2\2D\u01c1\3\2\2\2F\u01cd\3\2\2\2")
        buf.write("H\u01cf\3\2\2\2J\u01d1\3\2\2\2L\u01d3\3\2\2\2N\u01d5\3")
        buf.write("\2\2\2P\u01d7\3\2\2\2R\u01d9\3\2\2\2T\u01db\3\2\2\2V\u01dd")
        buf.write("\3\2\2\2X\u01e7\3\2\2\2Z\u01eb\3\2\2\2\\\u01fa\3\2\2\2")
        buf.write("^\u01fc\3\2\2\2`b\5\4\3\2a`\3\2\2\2ab\3\2\2\2bd\3\2\2")
        buf.write("\2ce\7\27\2\2dc\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\7\2\2\3")
        buf.write("g\3\3\2\2\2hj\5\6\4\2ik\7\27\2\2ji\3\2\2\2jk\3\2\2\2k")
        buf.write("m\3\2\2\2ln\7*\2\2ml\3\2\2\2mn\3\2\2\2nq\3\2\2\2oq\5\b")
        buf.write("\5\2ph\3\2\2\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2")
        buf.write("s}\3\2\2\2tr\3\2\2\2uz\5\6\4\2vx\7\27\2\2wv\3\2\2\2wx")
        buf.write("\3\2\2\2xy\3\2\2\2y{\7*\2\2zw\3\2\2\2z{\3\2\2\2{~\3\2")
        buf.write("\2\2|~\5\b\5\2}u\3\2\2\2}|\3\2\2\2~\5\3\2\2\2\177\u0080")
        buf.write("\5\n\6\2\u0080\7\3\2\2\2\u0081\u0082\7*\2\2\u0082\t\3")
        buf.write("\2\2\2\u0083\u0088\5\f\7\2\u0084\u0088\5\16\b\2\u0085")
        buf.write("\u0088\5\20\t\2\u0086\u0088\5\22\n\2\u0087\u0083\3\2\2")
        buf.write("\2\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\13\3\2\2\2\u0089\u008a\7\u00b8\2\2\u008a")
        buf.write("\u008b\5\26\f\2\u008b\u008c\7l\2\2\u008c\u008e\5\32\16")
        buf.write("\2\u008d\u008f\5,\27\2\u008e\u008d\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u0092\5V,\2\u0091\u0090")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093")
        buf.write("\u0095\5Z.\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0097\3\2\2\2\u0096\u0098\5\\/\2\u0097\u0096\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\r\3\2\2\2\u0099\u009b\7{\2")
        buf.write("\2\u009a\u009c\7u\2\2\u009b\u009a\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\7}\2\2\u009e")
        buf.write("\u00a3\5\32\16\2\u009f\u00a0\7\'\2\2\u00a0\u00a1\5&\24")
        buf.write("\2\u00a1\u00a2\7(\2\2\u00a2\u00a4\3\2\2\2\u00a3\u009f")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a6\t\2\2\2\u00a6\u00a7\5\24\13\2\u00a7\17\3\2\2\2")
        buf.write("\u00a8\u00aa\7\u00d5\2\2\u00a9\u00ab\7u\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ad\5\32\16\2\u00ad\u00ae\7\u00b9\2\2\u00ae\u00b3\5")
        buf.write("*\26\2\u00af\u00b0\7)\2\2\u00b0\u00b2\5*\26\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b6\u00b8\5,\27\2\u00b7\u00b6\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00bb\5V,\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00be\5Z.\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\21\3\2\2\2\u00bf\u00c1\7V\2\2\u00c0\u00c2\7u\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2")
        buf.write("\u00c3\u00c5\5\36\20\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\7l\2\2\u00c7")
        buf.write("\u00c9\5\32\16\2\u00c8\u00ca\5,\27\2\u00c9\u00c8\3\2\2")
        buf.write("\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00cd")
        buf.write("\5V,\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d0")
        buf.write("\3\2\2\2\u00ce\u00cf\7\u0088\2\2\u00cf\u00d1\5R*\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\23\3\2\2\2\u00d2")
        buf.write("\u00d3\7\'\2\2\u00d3\u00d4\5.\30\2\u00d4\u00d5\7(\2\2")
        buf.write("\u00d5\u00dd\3\2\2\2\u00d6\u00d7\7)\2\2\u00d7\u00d8\7")
        buf.write("\'\2\2\u00d8\u00d9\5.\30\2\u00d9\u00da\7(\2\2\u00da\u00dc")
        buf.write("\3\2\2\2\u00db\u00d6\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\25\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00e0\u00e3\7\23\2\2\u00e1\u00e3\5\30\r")
        buf.write("\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e8")
        buf.write("\3\2\2\2\u00e4\u00e5\7)\2\2\u00e5\u00e7\5\30\r\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\27\3\2\2\2\u00ea\u00e8\3\2")
        buf.write("\2\2\u00eb\u00ec\5 \21\2\u00ec\u00ed\7&\2\2\u00ed\u00ee")
        buf.write("\7\23\2\2\u00ee\u00f7\3\2\2\2\u00ef\u00f4\5\"\22\2\u00f0")
        buf.write("\u00f2\79\2\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f3\3\2\2\2\u00f3\u00f5\5(\25\2\u00f4\u00f1\3")
        buf.write("\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6\u00eb")
        buf.write("\3\2\2\2\u00f6\u00ef\3\2\2\2\u00f7\31\3\2\2\2\u00f8\u00fd")
        buf.write("\5\34\17\2\u00f9\u00fb\79\2\2\u00fa\u00f9\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\5\36\20")
        buf.write("\2\u00fd\u00fa\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\33\3")
        buf.write("\2\2\2\u00ff\u0100\5 \21\2\u0100\35\3\2\2\2\u0101\u0102")
        buf.write("\5(\25\2\u0102\37\3\2\2\2\u0103\u0106\5(\25\2\u0104\u0105")
        buf.write("\7&\2\2\u0105\u0107\5(\25\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107!\3\2\2\2\u0108\u010d\5(\25\2\u0109")
        buf.write("\u010b\5$\23\2\u010a\u010c\5$\23\2\u010b\u010a\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u0109\3")
        buf.write("\2\2\2\u010d\u010e\3\2\2\2\u010e\u0115\3\2\2\2\u010f\u0110")
        buf.write("\13\2\2\2\u0110\u0112\5$\23\2\u0111\u0113\5$\23\2\u0112")
        buf.write("\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0115\3\2\2\2")
        buf.write("\u0114\u0108\3\2\2\2\u0114\u010f\3\2\2\2\u0115#\3\2\2")
        buf.write("\2\u0116\u011a\7\u0442\2\2\u0117\u0118\7&\2\2\u0118\u011a")
        buf.write("\5(\25\2\u0119\u0116\3\2\2\2\u0119\u0117\3\2\2\2\u011a")
        buf.write("%\3\2\2\2\u011b\u0120\5(\25\2\u011c\u011d\7)\2\2\u011d")
        buf.write("\u011f\5(\25\2\u011e\u011c\3\2\2\2\u011f\u0122\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\'\3\2\2")
        buf.write("\2\u0122\u0120\3\2\2\2\u0123\u0127\7\u0443\2\2\u0124\u0127")
        buf.write("\5D#\2\u0125\u0127\5P)\2\u0126\u0123\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0125\3\2\2\2\u0127)\3\2\2\2\u0128\u0129")
        buf.write("\5\"\22\2\u0129\u012c\7\33\2\2\u012a\u012d\5\60\31\2\u012b")
        buf.write("\u012d\7T\2\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d+\3\2\2\2\u012e\u012f\7\u00db\2\2\u012f\u0130\5")
        buf.write("\60\31\2\u0130-\3\2\2\2\u0131\u0136\5\60\31\2\u0132\u0133")
        buf.write("\7)\2\2\u0133\u0135\5\60\31\2\u0134\u0132\3\2\2\2\u0135")
        buf.write("\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2")
        buf.write("\u0137/\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a\b\31\1")
        buf.write("\2\u013a\u013c\5\62\32\2\u013b\u013d\7\u0095\2\2\u013c")
        buf.write("\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u013f\7v\2\2\u013f\u0140\7\'\2\2\u0140\u0141\5")
        buf.write(".\30\2\u0141\u0142\7(\2\2\u0142\u0162\3\2\2\2\u0143\u0144")
        buf.write("\5\62\32\2\u0144\u0145\5@!\2\u0145\u0146\5\62\32\2\u0146")
        buf.write("\u0162\3\2\2\2\u0147\u0148\5\62\32\2\u0148\u014a\7~\2")
        buf.write("\2\u0149\u014b\7\u0095\2\2\u014a\u0149\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\5H%\2\u014d\u0162")
        buf.write("\3\2\2\2\u014e\u0150\5\62\32\2\u014f\u0151\7\u0095\2\2")
        buf.write("\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\3")
        buf.write("\2\2\2\u0152\u0153\7<\2\2\u0153\u0154\5\62\32\2\u0154")
        buf.write("\u0155\78\2\2\u0155\u0156\5\62\32\2\u0156\u0162\3\2\2")
        buf.write("\2\u0157\u0159\5\62\32\2\u0158\u015a\7\u0095\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b\u015c\7\u0087\2\2\u015c\u015d\5\62\32\2\u015d\u0162")
        buf.write("\3\2\2\2\u015e\u015f\7\u0095\2\2\u015f\u0162\5\60\31\5")
        buf.write("\u0160\u0162\5\62\32\2\u0161\u0139\3\2\2\2\u0161\u0143")
        buf.write("\3\2\2\2\u0161\u0147\3\2\2\2\u0161\u014e\3\2\2\2\u0161")
        buf.write("\u0157\3\2\2\2\u0161\u015e\3\2\2\2\u0161\u0160\3\2\2\2")
        buf.write("\u0162\u0169\3\2\2\2\u0163\u0164\f\4\2\2\u0164\u0165\5")
        buf.write("B\"\2\u0165\u0166\5\60\31\5\u0166\u0168\3\2\2\2\u0167")
        buf.write("\u0163\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u0169\u016a\3\2\2\2\u016a\61\3\2\2\2\u016b\u0169\3\2")
        buf.write("\2\2\u016c\u0170\5\"\22\2\u016d\u0170\5F$\2\u016e\u0170")
        buf.write("\5\64\33\2\u016f\u016c\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170\63\3\2\2\2\u0171\u017a\58\35\2\u0172")
        buf.write("\u0173\5\66\34\2\u0173\u0175\7\'\2\2\u0174\u0176\5:\36")
        buf.write("\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0178\7(\2\2\u0178\u017a\3\2\2\2\u0179")
        buf.write("\u0171\3\2\2\2\u0179\u0172\3\2\2\2\u017a\65\3\2\2\2\u017b")
        buf.write("\u0193\5> \2\u017c\u0193\7\u02d7\2\2\u017d\u0193\7\u014c")
        buf.write("\2\2\u017e\u0193\7\u0148\2\2\u017f\u0193\7\u0149\2\2\u0180")
        buf.write("\u0193\7\u014a\2\2\u0181\u0193\7\u014d\2\2\u0182\u0193")
        buf.write("\7\u014e\2\2\u0183\u0193\7\u014f\2\2\u0184\u0193\7t\2")
        buf.write("\2\u0185\u0193\7{\2\2\u0186\u0193\7\u014b\2\2\u0187\u0193")
        buf.write("\7\u0151\2\2\u0188\u0193\7\u0202\2\2\u0189\u0193\7\u0152")
        buf.write("\2\2\u018a\u0193\7\u00ae\2\2\u018b\u0193\7\u0154\2\2\u018c")
        buf.write("\u0193\7\u0155\2\2\u018d\u0193\7\u0156\2\2\u018e\u0193")
        buf.write("\7\u0157\2\2\u018f\u0193\7\u0158\2\2\u0190\u0193\7\u0159")
        buf.write("\2\2\u0191\u0193\7\u015a\2\2\u0192\u017b\3\2\2\2\u0192")
        buf.write("\u017c\3\2\2\2\u0192\u017d\3\2\2\2\u0192\u017e\3\2\2\2")
        buf.write("\u0192\u017f\3\2\2\2\u0192\u0180\3\2\2\2\u0192\u0181\3")
        buf.write("\2\2\2\u0192\u0182\3\2\2\2\u0192\u0183\3\2\2\2\u0192\u0184")
        buf.write("\3\2\2\2\u0192\u0185\3\2\2\2\u0192\u0186\3\2\2\2\u0192")
        buf.write("\u0187\3\2\2\2\u0192\u0188\3\2\2\2\u0192\u0189\3\2\2\2")
        buf.write("\u0192\u018a\3\2\2\2\u0192\u018b\3\2\2\2\u0192\u018c\3")
        buf.write("\2\2\2\u0192\u018d\3\2\2\2\u0192\u018e\3\2\2\2\u0192\u018f")
        buf.write("\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\67\3\2\2\2\u0194\u0197\t\3\2\2\u0195\u0196\7\'\2\2\u0196")
        buf.write("\u0198\7(\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u01989\3\2\2\2\u0199\u019e\5<\37\2\u019a\u019b\7)\2\2")
        buf.write("\u019b\u019d\5<\37\2\u019c\u019a\3\2\2\2\u019d\u01a0\3")
        buf.write("\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f;")
        buf.write("\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a5\5F$\2\u01a2\u01a5")
        buf.write("\5\"\22\2\u01a3\u01a5\5\64\33\2\u01a4\u01a1\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5=\3\2\2\2\u01a6")
        buf.write("\u01a7\t\4\2\2\u01a7?\3\2\2\2\u01a8\u01b7\7\33\2\2\u01a9")
        buf.write("\u01b7\7\34\2\2\u01aa\u01b7\7\36\2\2\u01ab\u01ac\7\36")
        buf.write("\2\2\u01ac\u01b7\7\33\2\2\u01ad\u01ae\7\34\2\2\u01ae\u01b7")
        buf.write("\7\33\2\2\u01af\u01b0\7\36\2\2\u01b0\u01b7\7\34\2\2\u01b1")
        buf.write("\u01b2\7 \2\2\u01b2\u01b7\7\33\2\2\u01b3\u01b4\7\36\2")
        buf.write("\2\u01b4\u01b5\7\33\2\2\u01b5\u01b7\7\34\2\2\u01b6\u01a8")
        buf.write("\3\2\2\2\u01b6\u01a9\3\2\2\2\u01b6\u01aa\3\2\2\2\u01b6")
        buf.write("\u01ab\3\2\2\2\u01b6\u01ad\3\2\2\2\u01b6\u01af\3\2\2\2")
        buf.write("\u01b6\u01b1\3\2\2\2\u01b6\u01b3\3\2\2\2\u01b7A\3\2\2")
        buf.write("\2\u01b8\u01c0\78\2\2\u01b9\u01ba\7$\2\2\u01ba\u01c0\7")
        buf.write("$\2\2\u01bb\u01c0\7\u00df\2\2\u01bc\u01c0\7\u009d\2\2")
        buf.write("\u01bd\u01be\7#\2\2\u01be\u01c0\7#\2\2\u01bf\u01b8\3\2")
        buf.write("\2\2\u01bf\u01b9\3\2\2\2\u01bf\u01bb\3\2\2\2\u01bf\u01bc")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0C\3\2\2\2\u01c1\u01c2")
        buf.write("\t\5\2\2\u01c2E\3\2\2\2\u01c3\u01ce\5^\60\2\u01c4\u01ce")
        buf.write("\5P)\2\u01c5\u01ce\5R*\2\u01c6\u01c7\7\30\2\2\u01c7\u01ce")
        buf.write("\5R*\2\u01c8\u01ce\5T+\2\u01c9\u01ce\5N(\2\u01ca\u01ce")
        buf.write("\5J&\2\u01cb\u01ce\5L\'\2\u01cc\u01ce\5H%\2\u01cd\u01c3")
        buf.write("\3\2\2\2\u01cd\u01c4\3\2\2\2\u01cd\u01c5\3\2\2\2\u01cd")
        buf.write("\u01c6\3\2\2\2\u01cd\u01c8\3\2\2\2\u01cd\u01c9\3\2\2\2")
        buf.write("\u01cd\u01ca\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01cc\3")
        buf.write("\2\2\2\u01ceG\3\2\2\2\u01cf\u01d0\7\u0097\2\2\u01d0I\3")
        buf.write("\2\2\2\u01d1\u01d2\7\u043f\2\2\u01d2K\3\2\2\2\u01d3\u01d4")
        buf.write("\7\u0441\2\2\u01d4M\3\2\2\2\u01d5\u01d6\t\6\2\2\u01d6")
        buf.write("O\3\2\2\2\u01d7\u01d8\7\u043c\2\2\u01d8Q\3\2\2\2\u01d9")
        buf.write("\u01da\t\7\2\2\u01daS\3\2\2\2\u01db\u01dc\7\u043e\2\2")
        buf.write("\u01dcU\3\2\2\2\u01dd\u01de\7\u009e\2\2\u01de\u01df\7")
        buf.write(">\2\2\u01df\u01e4\5X-\2\u01e0\u01e1\7)\2\2\u01e1\u01e3")
        buf.write("\5X-\2\u01e2\u01e0\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5W\3\2\2\2\u01e6\u01e4")
        buf.write("\3\2\2\2\u01e7\u01e9\5\60\31\2\u01e8\u01ea\t\b\2\2\u01e9")
        buf.write("\u01e8\3\2\2\2\u01e9\u01ea\3\2\2\2\u01eaY\3\2\2\2\u01eb")
        buf.write("\u01f0\7\u0088\2\2\u01ec\u01ee\5R*\2\u01ed\u01ec\3\2\2")
        buf.write("\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f1")
        buf.write("\7)\2\2\u01f0\u01ed\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u01f3\5R*\2\u01f3[\3\2\2\2\u01f4")
        buf.write("\u01f5\7i\2\2\u01f5\u01fb\7\u00d5\2\2\u01f6\u01f7\7\u008c")
        buf.write("\2\2\u01f7\u01f8\7v\2\2\u01f8\u01f9\7\u0259\2\2\u01f9")
        buf.write("\u01fb\7\u0205\2\2\u01fa\u01f4\3\2\2\2\u01fa\u01f6\3\2")
        buf.write("\2\2\u01fb]\3\2\2\2\u01fc\u01fd\t\t\2\2\u01fd_\3\2\2\2")
        buf.write("Cadjmprwz}\u0087\u008e\u0091\u0094\u0097\u009b\u00a3\u00aa")
        buf.write("\u00b3\u00b7\u00ba\u00bd\u00c1\u00c4\u00c9\u00cc\u00d0")
        buf.write("\u00dd\u00e2\u00e8\u00f1\u00f4\u00f6\u00fa\u00fd\u0106")
        buf.write("\u010b\u010d\u0112\u0114\u0119\u0120\u0126\u012c\u0136")
        buf.write("\u013c\u014a\u0150\u0159\u0161\u0169\u016f\u0175\u0179")
        buf.write("\u0192\u0197\u019e\u01a4\u01b6\u01bf\u01cd\u01e4\u01e9")
        buf.write("\u01ed\u01f0\u01fa")
        return buf.getvalue()


class MySqlBaseParser ( Parser ):

    grammarFileName = "MySqlBaseParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'?'", "<INVALID>", "<INVALID>", "':='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'&='", "'^='", 
                     "'|='", "'*'", "'/'", "'%'", "'+'", "'--'", "'-'", 
                     "'DIV'", "'MOD'", "'='", "'>'", "'>='", "'<'", "'<='", 
                     "'!'", "<INVALID>", "'~'", "'|'", "'&'", "'^'", "'.'", 
                     "'('", "')'", "','", "';'", "'@'", "'0'", "'1'", "'2'", 
                     "'''", "'\"'", "'`'", "':'" ]

    symbolicNames = [ "<INVALID>", "SPACE", "SPEC_MYSQL_COMMENT", "COMMENT_INPUT", 
                      "LINE_COMMENT", "QUESTION_", "PERCENT_S_", "PERCENT_NAME_", 
                      "VAR_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "XOR_ASSIGN", 
                      "OR_ASSIGN", "STAR", "DIVIDE", "MODULE", "PLUS", "MINUSMINUS", 
                      "MINUS", "DIV", "MOD", "EQUAL_SYMBOL", "GREATER_SYMBOL", 
                      "GREATER_EQUAL_SYMBOL", "LESS_SYMBOL", "LESS_EQUAL_SYMBOL", 
                      "EXCLAMATION_SYMBOL", "NOT_EQUAL_SYMBOL", "BIT_NOT_OP", 
                      "BIT_OR_OP", "BIT_AND_OP", "BIT_XOR_OP", "DOT", "LR_BRACKET", 
                      "RR_BRACKET", "COMMA", "SEMI", "AT_SIGN", "ZERO_DECIMAL", 
                      "ONE_DECIMAL", "TWO_DECIMAL", "SINGLE_QUOTE_SYMB", 
                      "DOUBLE_QUOTE_SYMB", "REVERSE_QUOTE_SYMB", "COLON_SYMB", 
                      "ADD", "ALL", "ALTER", "ALWAYS", "ANALYZE", "AND", 
                      "AS", "ASC", "BEFORE", "BETWEEN", "BOTH", "BY", "CALL", 
                      "CASCADE", "CASE", "CAST", "CHANGE", "CHARACTER", 
                      "CHECK", "COLLATE", "COLUMN", "CONDITION", "CONSTRAINT", 
                      "CONTINUE", "CONVERT", "CREATE", "CROSS", "CURRENT", 
                      "CURRENT_USER", "CURSOR", "DATABASE", "DATABASES", 
                      "DECLARE", "DEFAULT", "DELAYED", "DELETE", "DESC", 
                      "DESCRIBE", "DETERMINISTIC", "DIAGNOSTICS", "DISTINCT", 
                      "DISTINCTROW", "DROP", "EACH", "ELSE", "ELSEIF", "EMPTY", 
                      "ENCLOSED", "ESCAPED", "EXISTS", "EXIT", "EXPLAIN", 
                      "FALSE", "FETCH", "FOR", "FORCE", "FOREIGN", "FROM", 
                      "FULLTEXT", "GENERATED", "GET", "GRANT", "GROUP", 
                      "HAVING", "HIGH_PRIORITY", "IF", "IGNORE", "IN", "INDEX", 
                      "INFILE", "INNER", "INOUT", "INSERT", "INTERVAL", 
                      "INTO", "IS", "ITERATE", "JOIN", "KEY", "KEYS", "KILL", 
                      "LEADING", "LEAVE", "LEFT", "LIKE", "LIMIT", "LINEAR", 
                      "LINES", "LOAD", "LOCK", "LOOP", "LOW_PRIORITY", "MASTER_BIND", 
                      "MASTER_SSL_VERIFY_SERVER_CERT", "MATCH", "MAXVALUE", 
                      "MODIFIES", "NATURAL", "NOT", "NO_WRITE_TO_BINLOG", 
                      "NULL_LITERAL", "NUMBER", "ON", "OPTIMIZE", "OPTION", 
                      "OPTIONALLY", "OR", "ORDER", "OUT", "OUTER", "OUTFILE", 
                      "PARTITION", "PRIMARY", "PROCEDURE", "PURGE", "RANGE", 
                      "READ", "READS", "REFERENCES", "REGEXP", "RELEASE", 
                      "RENAME", "REPEAT", "REPLACE", "REQUIRE", "RESIGNAL", 
                      "RESTRICT", "RETURN", "REVOKE", "RIGHT", "RLIKE", 
                      "SCHEMA", "SCHEMAS", "SELECT", "SET", "SEPARATOR", 
                      "SHOW", "SIGNAL", "SPATIAL", "SQL", "SQLEXCEPTION", 
                      "SQLSTATE", "SQLWARNING", "SQL_BIG_RESULT", "SQL_CALC_FOUND_ROWS", 
                      "SQL_SMALL_RESULT", "SSL", "STACKED", "STARTING", 
                      "STRAIGHT_JOIN", "TABLE", "TERMINATED", "THEN", "TO", 
                      "TRAILING", "TRIGGER", "TRUE", "UNDO", "UNION", "UNIQUE", 
                      "UNLOCK", "UNSIGNED", "UPDATE", "USAGE", "USE", "USING", 
                      "VALUES", "WHEN", "WHERE", "WHILE", "WITH", "WRITE", 
                      "XOR", "ZEROFILL", "TINYINT", "SMALLINT", "MEDIUMINT", 
                      "MIDDLEINT", "INT", "INT1", "INT2", "INT3", "INT4", 
                      "INT8", "INTEGER", "BIGINT", "REAL", "DOUBLE", "PRECISION", 
                      "FLOAT", "FLOAT4", "FLOAT8", "DECIMAL", "DEC", "NUMERIC", 
                      "DATE", "TIME", "TIMESTAMP", "DATETIME", "YEAR", "CHAR", 
                      "VARCHAR", "NVARCHAR", "NATIONAL", "BINARY", "VARBINARY", 
                      "TINYBLOB", "BLOB", "MEDIUMBLOB", "LONG", "LONGBLOB", 
                      "TINYTEXT", "TEXT", "MEDIUMTEXT", "LONGTEXT", "ENUM", 
                      "VARYING", "SERIAL", "YEAR_MONTH", "DAY_HOUR", "DAY_MINUTE", 
                      "DAY_SECOND", "HOUR_MINUTE", "HOUR_SECOND", "MINUTE_SECOND", 
                      "SECOND_MICROSECOND", "MINUTE_MICROSECOND", "HOUR_MICROSECOND", 
                      "DAY_MICROSECOND", "JSON_ARRAY", "JSON_OBJECT", "JSON_QUOTE", 
                      "JSON_CONTAINS", "JSON_CONTAINS_PATH", "JSON_EXTRACT", 
                      "JSON_KEYS", "JSON_OVERLAPS", "JSON_SEARCH", "JSON_VALUE", 
                      "JSON_ARRAY_APPEND", "JSON_ARRAY_INSERT", "JSON_INSERT", 
                      "JSON_MERGE", "JSON_MERGE_PATCH", "JSON_MERGE_PRESERVE", 
                      "JSON_REMOVE", "JSON_REPLACE", "JSON_SET", "JSON_UNQUOTE", 
                      "JSON_DEPTH", "JSON_LENGTH", "JSON_TYPE", "JSON_VALID", 
                      "JSON_TABLE", "JSON_SCHEMA_VALID", "JSON_SCHEMA_VALIDATION_REPORT", 
                      "JSON_PRETTY", "JSON_STORAGE_FREE", "JSON_STORAGE_SIZE", 
                      "JSON_ARRAYAGG", "JSON_OBJECTAGG", "AVG", "BIT_AND", 
                      "BIT_OR", "BIT_XOR", "COUNT", "GROUP_CONCAT", "MAX", 
                      "MIN", "STD", "STDDEV", "STDDEV_POP", "STDDEV_SAMP", 
                      "SUM", "VAR_POP", "VAR_SAMP", "VARIANCE", "CURRENT_DATE", 
                      "CURRENT_TIME", "CURRENT_TIMESTAMP", "LOCALTIME", 
                      "CURDATE", "CURTIME", "DATE_ADD", "DATE_SUB", "EXTRACT", 
                      "LOCALTIMESTAMP", "NOW", "POSITION", "SUBSTR", "SUBSTRING", 
                      "SYSDATE", "TRIM", "UTC_DATE", "UTC_TIME", "UTC_TIMESTAMP", 
                      "ACCOUNT", "ACTION", "AFTER", "AGGREGATE", "ALGORITHM", 
                      "ANY", "AT", "AUTHORS", "AUTOCOMMIT", "AUTOEXTEND_SIZE", 
                      "AUTO_INCREMENT", "AVG_ROW_LENGTH", "BEGIN", "BINLOG", 
                      "BIT", "BLOCK", "BOOL", "BOOLEAN", "BTREE", "CACHE", 
                      "CASCADED", "CHAIN", "CHANGED", "CHANNEL", "CHECKSUM", 
                      "PAGE_CHECKSUM", "CIPHER", "CLASS_ORIGIN", "CLIENT", 
                      "CLOSE", "COALESCE", "CODE", "COLUMNS", "COLUMN_FORMAT", 
                      "COLUMN_NAME", "COMMENT", "COMMIT", "COMPACT", "COMPLETION", 
                      "COMPRESSED", "COMPRESSION", "CONCURRENT", "CONNECT", 
                      "CONNECTION", "CONSISTENT", "CONSTRAINT_CATALOG", 
                      "CONSTRAINT_SCHEMA", "CONSTRAINT_NAME", "CONTAINS", 
                      "CONTEXT", "CONTRIBUTORS", "COPY", "CPU", "CURSOR_NAME", 
                      "DATA", "DATAFILE", "DEALLOCATE", "DEFAULT_AUTH", 
                      "DEFINER", "DELAY_KEY_WRITE", "DES_KEY_FILE", "DIRECTORY", 
                      "DISABLE", "DISCARD", "DISK", "DO", "DUMPFILE", "DUPLICATE", 
                      "DYNAMIC", "ENABLE", "ENCRYPTION", "END", "ENDS", 
                      "ENGINE", "ENGINES", "ERROR", "ERRORS", "ESCAPE", 
                      "EVEN", "EVENT", "EVENTS", "EVERY", "EXCHANGE", "EXCLUSIVE", 
                      "EXPIRE", "EXPORT", "EXTENDED", "EXTENT_SIZE", "FAST", 
                      "FAULTS", "FIELDS", "FILE_BLOCK_SIZE", "FILTER", "FIRST", 
                      "FIXED", "FLUSH", "FOLLOWS", "FOUND", "FULL", "FUNCTION", 
                      "GENERAL", "GLOBAL", "GRANTS", "GROUP_REPLICATION", 
                      "HANDLER", "HASH", "HELP", "HOST", "HOSTS", "IDENTIFIED", 
                      "IGNORE_SERVER_IDS", "IMPORT", "INDEXES", "INITIAL_SIZE", 
                      "INPLACE", "INSERT_METHOD", "INSTALL", "INSTANCE", 
                      "INVISIBLE", "INVOKER", "IO", "IO_THREAD", "IPC", 
                      "ISOLATION", "ISSUER", "JSON", "KEY_BLOCK_SIZE", "LANGUAGE", 
                      "LAST", "LEAVES", "LESS", "LEVEL", "LIST", "LOCAL", 
                      "LOGFILE", "LOGS", "MASTER", "MASTER_AUTO_POSITION", 
                      "MASTER_CONNECT_RETRY", "MASTER_DELAY", "MASTER_HEARTBEAT_PERIOD", 
                      "MASTER_HOST", "MASTER_LOG_FILE", "MASTER_LOG_POS", 
                      "MASTER_PASSWORD", "MASTER_PORT", "MASTER_RETRY_COUNT", 
                      "MASTER_SSL", "MASTER_SSL_CA", "MASTER_SSL_CAPATH", 
                      "MASTER_SSL_CERT", "MASTER_SSL_CIPHER", "MASTER_SSL_CRL", 
                      "MASTER_SSL_CRLPATH", "MASTER_SSL_KEY", "MASTER_TLS_VERSION", 
                      "MASTER_USER", "MAX_CONNECTIONS_PER_HOUR", "MAX_QUERIES_PER_HOUR", 
                      "MAX_ROWS", "MAX_SIZE", "MAX_UPDATES_PER_HOUR", "MAX_USER_CONNECTIONS", 
                      "MEDIUM", "MEMBER", "MERGE", "MESSAGE_TEXT", "MID", 
                      "MIGRATE", "MIN_ROWS", "MODE", "MODIFY", "MUTEX", 
                      "MYSQL", "MYSQL_ERRNO", "NAME", "NAMES", "NCHAR", 
                      "NEVER", "NEXT", "NO", "NODEGROUP", "NONE", "ODBC", 
                      "OFFLINE", "OFFSET", "OF", "OJ", "OLD_PASSWORD", "ONE", 
                      "ONLINE", "ONLY", "OPEN", "OPTIMIZER_COSTS", "OPTIONS", 
                      "OWNER", "PACK_KEYS", "PAGE", "PARSER", "PARTIAL", 
                      "PARTITIONING", "PARTITIONS", "PASSWORD", "PHASE", 
                      "PLUGIN", "PLUGIN_DIR", "PLUGINS", "PORT", "PRECEDES", 
                      "PREPARE", "PRESERVE", "PREV", "PROCESSLIST", "PROFILE", 
                      "PROFILES", "PROXY", "QUERY", "QUICK", "REBUILD", 
                      "RECOVER", "REDO_BUFFER_SIZE", "REDUNDANT", "RELAY", 
                      "RELAY_LOG_FILE", "RELAY_LOG_POS", "RELAYLOG", "REMOVE", 
                      "REORGANIZE", "REPAIR", "REPLICATE_DO_DB", "REPLICATE_DO_TABLE", 
                      "REPLICATE_IGNORE_DB", "REPLICATE_IGNORE_TABLE", "REPLICATE_REWRITE_DB", 
                      "REPLICATE_WILD_DO_TABLE", "REPLICATE_WILD_IGNORE_TABLE", 
                      "REPLICATION", "RESET", "RESUME", "RETURNED_SQLSTATE", 
                      "RETURNING", "RETURNS", "ROLE", "ROLLBACK", "ROLLUP", 
                      "ROTATE", "ROW", "ROWS", "ROW_FORMAT", "SAVEPOINT", 
                      "SCHEDULE", "SECURITY", "SERVER", "SESSION", "SHARE", 
                      "SHARED", "SIGNED", "SIMPLE", "SLAVE", "SLOW", "SNAPSHOT", 
                      "SOCKET", "SOME", "SONAME", "SOUNDS", "SOURCE", "SQL_AFTER_GTIDS", 
                      "SQL_AFTER_MTS_GAPS", "SQL_BEFORE_GTIDS", "SQL_BUFFER_RESULT", 
                      "SQL_CACHE", "SQL_NO_CACHE", "SQL_THREAD", "START", 
                      "STARTS", "STATS_AUTO_RECALC", "STATS_PERSISTENT", 
                      "STATS_SAMPLE_PAGES", "STATUS", "STOP", "STORAGE", 
                      "STORED", "STRING", "SUBCLASS_ORIGIN", "SUBJECT", 
                      "SUBPARTITION", "SUBPARTITIONS", "SUSPEND", "SWAPS", 
                      "SWITCHES", "TABLE_NAME", "TABLESPACE", "TABLE_TYPE", 
                      "TEMPORARY", "TEMPTABLE", "THAN", "TRADITIONAL", "TRANSACTION", 
                      "TRANSACTIONAL", "TRIGGERS", "TRUNCATE", "UNDEFINED", 
                      "UNDOFILE", "UNDO_BUFFER_SIZE", "UNINSTALL", "UNKNOWN", 
                      "UNTIL", "UPGRADE", "USER", "USE_FRM", "USER_RESOURCES", 
                      "VALIDATION", "VALUE", "VARIABLES", "VIEW", "VIRTUAL", 
                      "VISIBLE", "WAIT", "WARNINGS", "WITHOUT", "WORK", 
                      "WRAPPER", "X509", "XA", "XML", "EUR", "USA", "JIS", 
                      "ISO", "INTERNAL", "QUARTER", "MONTH", "DAY", "HOUR", 
                      "MINUTE", "WEEK", "SECOND", "MICROSECOND", "TABLES", 
                      "ROUTINE", "EXECUTE", "FILE", "PROCESS", "RELOAD", 
                      "SHUTDOWN", "SUPER", "PRIVILEGES", "APPLICATION_PASSWORD_ADMIN", 
                      "AUDIT_ADMIN", "BACKUP_ADMIN", "BINLOG_ADMIN", "BINLOG_ENCRYPTION_ADMIN", 
                      "CLONE_ADMIN", "CONNECTION_ADMIN", "ENCRYPTION_KEY_ADMIN", 
                      "FIREWALL_ADMIN", "FIREWALL_USER", "FLUSH_OPTIMIZER_COSTS", 
                      "FLUSH_STATUS", "FLUSH_TABLES", "FLUSH_USER_RESOURCES", 
                      "GROUP_REPLICATION_ADMIN", "INNODB_REDO_LOG_ARCHIVE", 
                      "INNODB_REDO_LOG_ENABLE", "NDB_STORED_USER", "PERSIST_RO_VARIABLES_ADMIN", 
                      "REPLICATION_APPLIER", "REPLICATION_SLAVE_ADMIN", 
                      "RESOURCE_GROUP_ADMIN", "RESOURCE_GROUP_USER", "ROLE_ADMIN", 
                      "SERVICE_CONNECTION_ADMIN", "SESSION_VARIABLES_ADMIN", 
                      "SET_USER_ID", "SHOW_ROUTINE", "SYSTEM_VARIABLES_ADMIN", 
                      "TABLE_ENCRYPTION_ADMIN", "VERSION_TOKEN_ADMIN", "XA_RECOVER_ADMIN", 
                      "ARMSCII8", "ASCII", "BIG5", "CP1250", "CP1251", "CP1256", 
                      "CP1257", "CP850", "CP852", "CP866", "CP932", "DEC8", 
                      "EUCJPMS", "EUCKR", "GB2312", "GBK", "GEOSTD8", "GREEK", 
                      "HEBREW", "HP8", "KEYBCS2", "KOI8R", "KOI8U", "LATIN1", 
                      "LATIN2", "LATIN5", "LATIN7", "MACCE", "MACROMAN", 
                      "SJIS", "SWE7", "TIS620", "UCS2", "UJIS", "UTF16", 
                      "UTF16LE", "UTF32", "UTF8", "UTF8MB3", "UTF8MB4", 
                      "ARCHIVE", "BLACKHOLE", "CSV", "FEDERATED", "INNODB", 
                      "MEMORY", "MRG_MYISAM", "MYISAM", "NDB", "NDBCLUSTER", 
                      "PERFORMANCE_SCHEMA", "TOKUDB", "REPEATABLE", "COMMITTED", 
                      "UNCOMMITTED", "SERIALIZABLE", "GEOMETRYCOLLECTION", 
                      "GEOMCOLLECTION", "GEOMETRY", "LINESTRING", "MULTILINESTRING", 
                      "MULTIPOINT", "MULTIPOLYGON", "POINT", "POLYGON", 
                      "ABS", "ACOS", "ADDDATE", "ADDTIME", "AES_DECRYPT", 
                      "AES_ENCRYPT", "AREA", "ASBINARY", "ASIN", "ASTEXT", 
                      "ASWKB", "ASWKT", "ASYMMETRIC_DECRYPT", "ASYMMETRIC_DERIVE", 
                      "ASYMMETRIC_ENCRYPT", "ASYMMETRIC_SIGN", "ASYMMETRIC_VERIFY", 
                      "ATAN", "ATAN2", "BENCHMARK", "BIN", "BIT_COUNT", 
                      "BIT_LENGTH", "BUFFER", "CATALOG_NAME", "CEIL", "CEILING", 
                      "CENTROID", "CHARACTER_LENGTH", "CHARSET", "CHAR_LENGTH", 
                      "COERCIBILITY", "COLLATION", "COMPRESS", "CONCAT", 
                      "CONCAT_WS", "CONNECTION_ID", "CONV", "CONVERT_TZ", 
                      "COS", "COT", "CRC32", "CREATE_ASYMMETRIC_PRIV_KEY", 
                      "CREATE_ASYMMETRIC_PUB_KEY", "CREATE_DH_PARAMETERS", 
                      "CREATE_DIGEST", "CROSSES", "DATEDIFF", "DATE_FORMAT", 
                      "DAYNAME", "DAYOFMONTH", "DAYOFWEEK", "DAYOFYEAR", 
                      "DECODE", "DEGREES", "DES_DECRYPT", "DES_ENCRYPT", 
                      "DIMENSION", "DISJOINT", "ELT", "ENCODE", "ENCRYPT", 
                      "ENDPOINT", "ENVELOPE", "EQUALS", "EXP", "EXPORT_SET", 
                      "EXTERIORRING", "EXTRACTVALUE", "FIELD", "FIND_IN_SET", 
                      "FLOOR", "FORMAT", "FOUND_ROWS", "FROM_BASE64", "FROM_DAYS", 
                      "FROM_UNIXTIME", "GEOMCOLLFROMTEXT", "GEOMCOLLFROMWKB", 
                      "GEOMETRYCOLLECTIONFROMTEXT", "GEOMETRYCOLLECTIONFROMWKB", 
                      "GEOMETRYFROMTEXT", "GEOMETRYFROMWKB", "GEOMETRYN", 
                      "GEOMETRYTYPE", "GEOMFROMTEXT", "GEOMFROMWKB", "GET_FORMAT", 
                      "GET_LOCK", "GLENGTH", "GREATEST", "GTID_SUBSET", 
                      "GTID_SUBTRACT", "HEX", "IFNULL", "INET6_ATON", "INET6_NTOA", 
                      "INET_ATON", "INET_NTOA", "INSTR", "INTERIORRINGN", 
                      "INTERSECTS", "ISCLOSED", "ISEMPTY", "ISNULL", "ISSIMPLE", 
                      "IS_FREE_LOCK", "IS_IPV4", "IS_IPV4_COMPAT", "IS_IPV4_MAPPED", 
                      "IS_IPV6", "IS_USED_LOCK", "LAST_INSERT_ID", "LCASE", 
                      "LEAST", "LENGTH", "LINEFROMTEXT", "LINEFROMWKB", 
                      "LINESTRINGFROMTEXT", "LINESTRINGFROMWKB", "LN", "LOAD_FILE", 
                      "LOCATE", "LOG", "LOG10", "LOG2", "LOWER", "LPAD", 
                      "LTRIM", "MAKEDATE", "MAKETIME", "MAKE_SET", "MASTER_POS_WAIT", 
                      "MBRCONTAINS", "MBRDISJOINT", "MBREQUAL", "MBRINTERSECTS", 
                      "MBROVERLAPS", "MBRTOUCHES", "MBRWITHIN", "MD5", "MLINEFROMTEXT", 
                      "MLINEFROMWKB", "MONTHNAME", "MPOINTFROMTEXT", "MPOINTFROMWKB", 
                      "MPOLYFROMTEXT", "MPOLYFROMWKB", "MULTILINESTRINGFROMTEXT", 
                      "MULTILINESTRINGFROMWKB", "MULTIPOINTFROMTEXT", "MULTIPOINTFROMWKB", 
                      "MULTIPOLYGONFROMTEXT", "MULTIPOLYGONFROMWKB", "NAME_CONST", 
                      "NULLIF", "NUMGEOMETRIES", "NUMINTERIORRINGS", "NUMPOINTS", 
                      "OCT", "OCTET_LENGTH", "ORD", "OVERLAPS", "PERIOD_ADD", 
                      "PERIOD_DIFF", "PI", "POINTFROMTEXT", "POINTFROMWKB", 
                      "POINTN", "POLYFROMTEXT", "POLYFROMWKB", "POLYGONFROMTEXT", 
                      "POLYGONFROMWKB", "POW", "POWER", "QUOTE", "RADIANS", 
                      "RAND", "RANDOM_BYTES", "RELEASE_LOCK", "REVERSE", 
                      "ROUND", "ROW_COUNT", "RPAD", "RTRIM", "SEC_TO_TIME", 
                      "SESSION_USER", "SHA", "SHA1", "SHA2", "SCHEMA_NAME", 
                      "SIGN", "SIN", "SLEEP", "SOUNDEX", "SQL_THREAD_WAIT_AFTER_GTIDS", 
                      "SQRT", "SRID", "STARTPOINT", "STRCMP", "STR_TO_DATE", 
                      "ST_AREA", "ST_ASBINARY", "ST_ASTEXT", "ST_ASWKB", 
                      "ST_ASWKT", "ST_BUFFER", "ST_CENTROID", "ST_CONTAINS", 
                      "ST_CROSSES", "ST_DIFFERENCE", "ST_DIMENSION", "ST_DISJOINT", 
                      "ST_DISTANCE", "ST_ENDPOINT", "ST_ENVELOPE", "ST_EQUALS", 
                      "ST_EXTERIORRING", "ST_GEOMCOLLFROMTEXT", "ST_GEOMCOLLFROMTXT", 
                      "ST_GEOMCOLLFROMWKB", "ST_GEOMETRYCOLLECTIONFROMTEXT", 
                      "ST_GEOMETRYCOLLECTIONFROMWKB", "ST_GEOMETRYFROMTEXT", 
                      "ST_GEOMETRYFROMWKB", "ST_GEOMETRYN", "ST_GEOMETRYTYPE", 
                      "ST_GEOMFROMTEXT", "ST_GEOMFROMWKB", "ST_INTERIORRINGN", 
                      "ST_INTERSECTION", "ST_INTERSECTS", "ST_ISCLOSED", 
                      "ST_ISEMPTY", "ST_ISSIMPLE", "ST_LINEFROMTEXT", "ST_LINEFROMWKB", 
                      "ST_LINESTRINGFROMTEXT", "ST_LINESTRINGFROMWKB", "ST_NUMGEOMETRIES", 
                      "ST_NUMINTERIORRING", "ST_NUMINTERIORRINGS", "ST_NUMPOINTS", 
                      "ST_OVERLAPS", "ST_POINTFROMTEXT", "ST_POINTFROMWKB", 
                      "ST_POINTN", "ST_POLYFROMTEXT", "ST_POLYFROMWKB", 
                      "ST_POLYGONFROMTEXT", "ST_POLYGONFROMWKB", "ST_SRID", 
                      "ST_STARTPOINT", "ST_SYMDIFFERENCE", "ST_TOUCHES", 
                      "ST_UNION", "ST_WITHIN", "ST_X", "ST_Y", "SUBDATE", 
                      "SUBSTRING_INDEX", "SUBTIME", "SYSTEM_USER", "TAN", 
                      "TIMEDIFF", "TIMESTAMPADD", "TIMESTAMPDIFF", "TIME_FORMAT", 
                      "TIME_TO_SEC", "TOUCHES", "TO_BASE64", "TO_DAYS", 
                      "TO_SECONDS", "UCASE", "UNCOMPRESS", "UNCOMPRESSED_LENGTH", 
                      "UNHEX", "UNIX_TIMESTAMP", "UPDATEXML", "UPPER", "UUID", 
                      "UUID_SHORT", "VALIDATE_PASSWORD_STRENGTH", "VERSION", 
                      "WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS", "WEEKDAY", "WEEKOFYEAR", 
                      "WEIGHT_STRING", "WITHIN", "YEARWEEK", "Y_FUNCTION", 
                      "X_FUNCTION", "START_NATIONAL_STRING_LITERAL", "STRING_LITERAL", 
                      "DECIMAL_LITERAL", "HEXADECIMAL_LITERAL", "REAL_LITERAL", 
                      "NULL_SPEC_LITERAL", "BIT_STRING", "DOT_ID", "ID", 
                      "REVERSE_QUOTE_ID", "ERROR_RECONGNIGION", "OPTIONAL" ]

    RULE_root = 0
    RULE_sqlStatements = 1
    RULE_sqlStatement = 2
    RULE_emptyStatement = 3
    RULE_dmlStatement = 4
    RULE_selectStatement = 5
    RULE_insertStatement = 6
    RULE_updateStatement = 7
    RULE_deleteStatement = 8
    RULE_insertStatementValue = 9
    RULE_selectElements = 10
    RULE_selectElement = 11
    RULE_tableSource = 12
    RULE_tableName = 13
    RULE_tableAlias = 14
    RULE_fullId = 15
    RULE_fullColumnName = 16
    RULE_dottedId = 17
    RULE_uidList = 18
    RULE_uid = 19
    RULE_updatedElement = 20
    RULE_whereClause = 21
    RULE_expressions = 22
    RULE_expression = 23
    RULE_predicate = 24
    RULE_functionCall = 25
    RULE_scalarFunctionName = 26
    RULE_specificFunction = 27
    RULE_functionArgs = 28
    RULE_functionArg = 29
    RULE_functionNameBase = 30
    RULE_comparisonOperator = 31
    RULE_logicalOperator = 32
    RULE_keywordsCanBeId = 33
    RULE_constant = 34
    RULE_nullLiteral = 35
    RULE_realLiteral = 36
    RULE_bitString = 37
    RULE_booleanLiteral = 38
    RULE_stringLiteral = 39
    RULE_decimalLiteral = 40
    RULE_hexadecimalLiteral = 41
    RULE_orderByClause = 42
    RULE_orderByExpression = 43
    RULE_limitClause = 44
    RULE_lockClause = 45
    RULE_parameterMarker = 46

    ruleNames =  [ "root", "sqlStatements", "sqlStatement", "emptyStatement", 
                   "dmlStatement", "selectStatement", "insertStatement", 
                   "updateStatement", "deleteStatement", "insertStatementValue", 
                   "selectElements", "selectElement", "tableSource", "tableName", 
                   "tableAlias", "fullId", "fullColumnName", "dottedId", 
                   "uidList", "uid", "updatedElement", "whereClause", "expressions", 
                   "expression", "predicate", "functionCall", "scalarFunctionName", 
                   "specificFunction", "functionArgs", "functionArg", "functionNameBase", 
                   "comparisonOperator", "logicalOperator", "keywordsCanBeId", 
                   "constant", "nullLiteral", "realLiteral", "bitString", 
                   "booleanLiteral", "stringLiteral", "decimalLiteral", 
                   "hexadecimalLiteral", "orderByClause", "orderByExpression", 
                   "limitClause", "lockClause", "parameterMarker" ]

    EOF = Token.EOF
    SPACE=1
    SPEC_MYSQL_COMMENT=2
    COMMENT_INPUT=3
    LINE_COMMENT=4
    QUESTION_=5
    PERCENT_S_=6
    PERCENT_NAME_=7
    VAR_ASSIGN=8
    PLUS_ASSIGN=9
    MINUS_ASSIGN=10
    MULT_ASSIGN=11
    DIV_ASSIGN=12
    MOD_ASSIGN=13
    AND_ASSIGN=14
    XOR_ASSIGN=15
    OR_ASSIGN=16
    STAR=17
    DIVIDE=18
    MODULE=19
    PLUS=20
    MINUSMINUS=21
    MINUS=22
    DIV=23
    MOD=24
    EQUAL_SYMBOL=25
    GREATER_SYMBOL=26
    GREATER_EQUAL_SYMBOL=27
    LESS_SYMBOL=28
    LESS_EQUAL_SYMBOL=29
    EXCLAMATION_SYMBOL=30
    NOT_EQUAL_SYMBOL=31
    BIT_NOT_OP=32
    BIT_OR_OP=33
    BIT_AND_OP=34
    BIT_XOR_OP=35
    DOT=36
    LR_BRACKET=37
    RR_BRACKET=38
    COMMA=39
    SEMI=40
    AT_SIGN=41
    ZERO_DECIMAL=42
    ONE_DECIMAL=43
    TWO_DECIMAL=44
    SINGLE_QUOTE_SYMB=45
    DOUBLE_QUOTE_SYMB=46
    REVERSE_QUOTE_SYMB=47
    COLON_SYMB=48
    ADD=49
    ALL=50
    ALTER=51
    ALWAYS=52
    ANALYZE=53
    AND=54
    AS=55
    ASC=56
    BEFORE=57
    BETWEEN=58
    BOTH=59
    BY=60
    CALL=61
    CASCADE=62
    CASE=63
    CAST=64
    CHANGE=65
    CHARACTER=66
    CHECK=67
    COLLATE=68
    COLUMN=69
    CONDITION=70
    CONSTRAINT=71
    CONTINUE=72
    CONVERT=73
    CREATE=74
    CROSS=75
    CURRENT=76
    CURRENT_USER=77
    CURSOR=78
    DATABASE=79
    DATABASES=80
    DECLARE=81
    DEFAULT=82
    DELAYED=83
    DELETE=84
    DESC=85
    DESCRIBE=86
    DETERMINISTIC=87
    DIAGNOSTICS=88
    DISTINCT=89
    DISTINCTROW=90
    DROP=91
    EACH=92
    ELSE=93
    ELSEIF=94
    EMPTY=95
    ENCLOSED=96
    ESCAPED=97
    EXISTS=98
    EXIT=99
    EXPLAIN=100
    FALSE=101
    FETCH=102
    FOR=103
    FORCE=104
    FOREIGN=105
    FROM=106
    FULLTEXT=107
    GENERATED=108
    GET=109
    GRANT=110
    GROUP=111
    HAVING=112
    HIGH_PRIORITY=113
    IF=114
    IGNORE=115
    IN=116
    INDEX=117
    INFILE=118
    INNER=119
    INOUT=120
    INSERT=121
    INTERVAL=122
    INTO=123
    IS=124
    ITERATE=125
    JOIN=126
    KEY=127
    KEYS=128
    KILL=129
    LEADING=130
    LEAVE=131
    LEFT=132
    LIKE=133
    LIMIT=134
    LINEAR=135
    LINES=136
    LOAD=137
    LOCK=138
    LOOP=139
    LOW_PRIORITY=140
    MASTER_BIND=141
    MASTER_SSL_VERIFY_SERVER_CERT=142
    MATCH=143
    MAXVALUE=144
    MODIFIES=145
    NATURAL=146
    NOT=147
    NO_WRITE_TO_BINLOG=148
    NULL_LITERAL=149
    NUMBER=150
    ON=151
    OPTIMIZE=152
    OPTION=153
    OPTIONALLY=154
    OR=155
    ORDER=156
    OUT=157
    OUTER=158
    OUTFILE=159
    PARTITION=160
    PRIMARY=161
    PROCEDURE=162
    PURGE=163
    RANGE=164
    READ=165
    READS=166
    REFERENCES=167
    REGEXP=168
    RELEASE=169
    RENAME=170
    REPEAT=171
    REPLACE=172
    REQUIRE=173
    RESIGNAL=174
    RESTRICT=175
    RETURN=176
    REVOKE=177
    RIGHT=178
    RLIKE=179
    SCHEMA=180
    SCHEMAS=181
    SELECT=182
    SET=183
    SEPARATOR=184
    SHOW=185
    SIGNAL=186
    SPATIAL=187
    SQL=188
    SQLEXCEPTION=189
    SQLSTATE=190
    SQLWARNING=191
    SQL_BIG_RESULT=192
    SQL_CALC_FOUND_ROWS=193
    SQL_SMALL_RESULT=194
    SSL=195
    STACKED=196
    STARTING=197
    STRAIGHT_JOIN=198
    TABLE=199
    TERMINATED=200
    THEN=201
    TO=202
    TRAILING=203
    TRIGGER=204
    TRUE=205
    UNDO=206
    UNION=207
    UNIQUE=208
    UNLOCK=209
    UNSIGNED=210
    UPDATE=211
    USAGE=212
    USE=213
    USING=214
    VALUES=215
    WHEN=216
    WHERE=217
    WHILE=218
    WITH=219
    WRITE=220
    XOR=221
    ZEROFILL=222
    TINYINT=223
    SMALLINT=224
    MEDIUMINT=225
    MIDDLEINT=226
    INT=227
    INT1=228
    INT2=229
    INT3=230
    INT4=231
    INT8=232
    INTEGER=233
    BIGINT=234
    REAL=235
    DOUBLE=236
    PRECISION=237
    FLOAT=238
    FLOAT4=239
    FLOAT8=240
    DECIMAL=241
    DEC=242
    NUMERIC=243
    DATE=244
    TIME=245
    TIMESTAMP=246
    DATETIME=247
    YEAR=248
    CHAR=249
    VARCHAR=250
    NVARCHAR=251
    NATIONAL=252
    BINARY=253
    VARBINARY=254
    TINYBLOB=255
    BLOB=256
    MEDIUMBLOB=257
    LONG=258
    LONGBLOB=259
    TINYTEXT=260
    TEXT=261
    MEDIUMTEXT=262
    LONGTEXT=263
    ENUM=264
    VARYING=265
    SERIAL=266
    YEAR_MONTH=267
    DAY_HOUR=268
    DAY_MINUTE=269
    DAY_SECOND=270
    HOUR_MINUTE=271
    HOUR_SECOND=272
    MINUTE_SECOND=273
    SECOND_MICROSECOND=274
    MINUTE_MICROSECOND=275
    HOUR_MICROSECOND=276
    DAY_MICROSECOND=277
    JSON_ARRAY=278
    JSON_OBJECT=279
    JSON_QUOTE=280
    JSON_CONTAINS=281
    JSON_CONTAINS_PATH=282
    JSON_EXTRACT=283
    JSON_KEYS=284
    JSON_OVERLAPS=285
    JSON_SEARCH=286
    JSON_VALUE=287
    JSON_ARRAY_APPEND=288
    JSON_ARRAY_INSERT=289
    JSON_INSERT=290
    JSON_MERGE=291
    JSON_MERGE_PATCH=292
    JSON_MERGE_PRESERVE=293
    JSON_REMOVE=294
    JSON_REPLACE=295
    JSON_SET=296
    JSON_UNQUOTE=297
    JSON_DEPTH=298
    JSON_LENGTH=299
    JSON_TYPE=300
    JSON_VALID=301
    JSON_TABLE=302
    JSON_SCHEMA_VALID=303
    JSON_SCHEMA_VALIDATION_REPORT=304
    JSON_PRETTY=305
    JSON_STORAGE_FREE=306
    JSON_STORAGE_SIZE=307
    JSON_ARRAYAGG=308
    JSON_OBJECTAGG=309
    AVG=310
    BIT_AND=311
    BIT_OR=312
    BIT_XOR=313
    COUNT=314
    GROUP_CONCAT=315
    MAX=316
    MIN=317
    STD=318
    STDDEV=319
    STDDEV_POP=320
    STDDEV_SAMP=321
    SUM=322
    VAR_POP=323
    VAR_SAMP=324
    VARIANCE=325
    CURRENT_DATE=326
    CURRENT_TIME=327
    CURRENT_TIMESTAMP=328
    LOCALTIME=329
    CURDATE=330
    CURTIME=331
    DATE_ADD=332
    DATE_SUB=333
    EXTRACT=334
    LOCALTIMESTAMP=335
    NOW=336
    POSITION=337
    SUBSTR=338
    SUBSTRING=339
    SYSDATE=340
    TRIM=341
    UTC_DATE=342
    UTC_TIME=343
    UTC_TIMESTAMP=344
    ACCOUNT=345
    ACTION=346
    AFTER=347
    AGGREGATE=348
    ALGORITHM=349
    ANY=350
    AT=351
    AUTHORS=352
    AUTOCOMMIT=353
    AUTOEXTEND_SIZE=354
    AUTO_INCREMENT=355
    AVG_ROW_LENGTH=356
    BEGIN=357
    BINLOG=358
    BIT=359
    BLOCK=360
    BOOL=361
    BOOLEAN=362
    BTREE=363
    CACHE=364
    CASCADED=365
    CHAIN=366
    CHANGED=367
    CHANNEL=368
    CHECKSUM=369
    PAGE_CHECKSUM=370
    CIPHER=371
    CLASS_ORIGIN=372
    CLIENT=373
    CLOSE=374
    COALESCE=375
    CODE=376
    COLUMNS=377
    COLUMN_FORMAT=378
    COLUMN_NAME=379
    COMMENT=380
    COMMIT=381
    COMPACT=382
    COMPLETION=383
    COMPRESSED=384
    COMPRESSION=385
    CONCURRENT=386
    CONNECT=387
    CONNECTION=388
    CONSISTENT=389
    CONSTRAINT_CATALOG=390
    CONSTRAINT_SCHEMA=391
    CONSTRAINT_NAME=392
    CONTAINS=393
    CONTEXT=394
    CONTRIBUTORS=395
    COPY=396
    CPU=397
    CURSOR_NAME=398
    DATA=399
    DATAFILE=400
    DEALLOCATE=401
    DEFAULT_AUTH=402
    DEFINER=403
    DELAY_KEY_WRITE=404
    DES_KEY_FILE=405
    DIRECTORY=406
    DISABLE=407
    DISCARD=408
    DISK=409
    DO=410
    DUMPFILE=411
    DUPLICATE=412
    DYNAMIC=413
    ENABLE=414
    ENCRYPTION=415
    END=416
    ENDS=417
    ENGINE=418
    ENGINES=419
    ERROR=420
    ERRORS=421
    ESCAPE=422
    EVEN=423
    EVENT=424
    EVENTS=425
    EVERY=426
    EXCHANGE=427
    EXCLUSIVE=428
    EXPIRE=429
    EXPORT=430
    EXTENDED=431
    EXTENT_SIZE=432
    FAST=433
    FAULTS=434
    FIELDS=435
    FILE_BLOCK_SIZE=436
    FILTER=437
    FIRST=438
    FIXED=439
    FLUSH=440
    FOLLOWS=441
    FOUND=442
    FULL=443
    FUNCTION=444
    GENERAL=445
    GLOBAL=446
    GRANTS=447
    GROUP_REPLICATION=448
    HANDLER=449
    HASH=450
    HELP=451
    HOST=452
    HOSTS=453
    IDENTIFIED=454
    IGNORE_SERVER_IDS=455
    IMPORT=456
    INDEXES=457
    INITIAL_SIZE=458
    INPLACE=459
    INSERT_METHOD=460
    INSTALL=461
    INSTANCE=462
    INVISIBLE=463
    INVOKER=464
    IO=465
    IO_THREAD=466
    IPC=467
    ISOLATION=468
    ISSUER=469
    JSON=470
    KEY_BLOCK_SIZE=471
    LANGUAGE=472
    LAST=473
    LEAVES=474
    LESS=475
    LEVEL=476
    LIST=477
    LOCAL=478
    LOGFILE=479
    LOGS=480
    MASTER=481
    MASTER_AUTO_POSITION=482
    MASTER_CONNECT_RETRY=483
    MASTER_DELAY=484
    MASTER_HEARTBEAT_PERIOD=485
    MASTER_HOST=486
    MASTER_LOG_FILE=487
    MASTER_LOG_POS=488
    MASTER_PASSWORD=489
    MASTER_PORT=490
    MASTER_RETRY_COUNT=491
    MASTER_SSL=492
    MASTER_SSL_CA=493
    MASTER_SSL_CAPATH=494
    MASTER_SSL_CERT=495
    MASTER_SSL_CIPHER=496
    MASTER_SSL_CRL=497
    MASTER_SSL_CRLPATH=498
    MASTER_SSL_KEY=499
    MASTER_TLS_VERSION=500
    MASTER_USER=501
    MAX_CONNECTIONS_PER_HOUR=502
    MAX_QUERIES_PER_HOUR=503
    MAX_ROWS=504
    MAX_SIZE=505
    MAX_UPDATES_PER_HOUR=506
    MAX_USER_CONNECTIONS=507
    MEDIUM=508
    MEMBER=509
    MERGE=510
    MESSAGE_TEXT=511
    MID=512
    MIGRATE=513
    MIN_ROWS=514
    MODE=515
    MODIFY=516
    MUTEX=517
    MYSQL=518
    MYSQL_ERRNO=519
    NAME=520
    NAMES=521
    NCHAR=522
    NEVER=523
    NEXT=524
    NO=525
    NODEGROUP=526
    NONE=527
    ODBC=528
    OFFLINE=529
    OFFSET=530
    OF=531
    OJ=532
    OLD_PASSWORD=533
    ONE=534
    ONLINE=535
    ONLY=536
    OPEN=537
    OPTIMIZER_COSTS=538
    OPTIONS=539
    OWNER=540
    PACK_KEYS=541
    PAGE=542
    PARSER=543
    PARTIAL=544
    PARTITIONING=545
    PARTITIONS=546
    PASSWORD=547
    PHASE=548
    PLUGIN=549
    PLUGIN_DIR=550
    PLUGINS=551
    PORT=552
    PRECEDES=553
    PREPARE=554
    PRESERVE=555
    PREV=556
    PROCESSLIST=557
    PROFILE=558
    PROFILES=559
    PROXY=560
    QUERY=561
    QUICK=562
    REBUILD=563
    RECOVER=564
    REDO_BUFFER_SIZE=565
    REDUNDANT=566
    RELAY=567
    RELAY_LOG_FILE=568
    RELAY_LOG_POS=569
    RELAYLOG=570
    REMOVE=571
    REORGANIZE=572
    REPAIR=573
    REPLICATE_DO_DB=574
    REPLICATE_DO_TABLE=575
    REPLICATE_IGNORE_DB=576
    REPLICATE_IGNORE_TABLE=577
    REPLICATE_REWRITE_DB=578
    REPLICATE_WILD_DO_TABLE=579
    REPLICATE_WILD_IGNORE_TABLE=580
    REPLICATION=581
    RESET=582
    RESUME=583
    RETURNED_SQLSTATE=584
    RETURNING=585
    RETURNS=586
    ROLE=587
    ROLLBACK=588
    ROLLUP=589
    ROTATE=590
    ROW=591
    ROWS=592
    ROW_FORMAT=593
    SAVEPOINT=594
    SCHEDULE=595
    SECURITY=596
    SERVER=597
    SESSION=598
    SHARE=599
    SHARED=600
    SIGNED=601
    SIMPLE=602
    SLAVE=603
    SLOW=604
    SNAPSHOT=605
    SOCKET=606
    SOME=607
    SONAME=608
    SOUNDS=609
    SOURCE=610
    SQL_AFTER_GTIDS=611
    SQL_AFTER_MTS_GAPS=612
    SQL_BEFORE_GTIDS=613
    SQL_BUFFER_RESULT=614
    SQL_CACHE=615
    SQL_NO_CACHE=616
    SQL_THREAD=617
    START=618
    STARTS=619
    STATS_AUTO_RECALC=620
    STATS_PERSISTENT=621
    STATS_SAMPLE_PAGES=622
    STATUS=623
    STOP=624
    STORAGE=625
    STORED=626
    STRING=627
    SUBCLASS_ORIGIN=628
    SUBJECT=629
    SUBPARTITION=630
    SUBPARTITIONS=631
    SUSPEND=632
    SWAPS=633
    SWITCHES=634
    TABLE_NAME=635
    TABLESPACE=636
    TABLE_TYPE=637
    TEMPORARY=638
    TEMPTABLE=639
    THAN=640
    TRADITIONAL=641
    TRANSACTION=642
    TRANSACTIONAL=643
    TRIGGERS=644
    TRUNCATE=645
    UNDEFINED=646
    UNDOFILE=647
    UNDO_BUFFER_SIZE=648
    UNINSTALL=649
    UNKNOWN=650
    UNTIL=651
    UPGRADE=652
    USER=653
    USE_FRM=654
    USER_RESOURCES=655
    VALIDATION=656
    VALUE=657
    VARIABLES=658
    VIEW=659
    VIRTUAL=660
    VISIBLE=661
    WAIT=662
    WARNINGS=663
    WITHOUT=664
    WORK=665
    WRAPPER=666
    X509=667
    XA=668
    XML=669
    EUR=670
    USA=671
    JIS=672
    ISO=673
    INTERNAL=674
    QUARTER=675
    MONTH=676
    DAY=677
    HOUR=678
    MINUTE=679
    WEEK=680
    SECOND=681
    MICROSECOND=682
    TABLES=683
    ROUTINE=684
    EXECUTE=685
    FILE=686
    PROCESS=687
    RELOAD=688
    SHUTDOWN=689
    SUPER=690
    PRIVILEGES=691
    APPLICATION_PASSWORD_ADMIN=692
    AUDIT_ADMIN=693
    BACKUP_ADMIN=694
    BINLOG_ADMIN=695
    BINLOG_ENCRYPTION_ADMIN=696
    CLONE_ADMIN=697
    CONNECTION_ADMIN=698
    ENCRYPTION_KEY_ADMIN=699
    FIREWALL_ADMIN=700
    FIREWALL_USER=701
    FLUSH_OPTIMIZER_COSTS=702
    FLUSH_STATUS=703
    FLUSH_TABLES=704
    FLUSH_USER_RESOURCES=705
    GROUP_REPLICATION_ADMIN=706
    INNODB_REDO_LOG_ARCHIVE=707
    INNODB_REDO_LOG_ENABLE=708
    NDB_STORED_USER=709
    PERSIST_RO_VARIABLES_ADMIN=710
    REPLICATION_APPLIER=711
    REPLICATION_SLAVE_ADMIN=712
    RESOURCE_GROUP_ADMIN=713
    RESOURCE_GROUP_USER=714
    ROLE_ADMIN=715
    SERVICE_CONNECTION_ADMIN=716
    SESSION_VARIABLES_ADMIN=717
    SET_USER_ID=718
    SHOW_ROUTINE=719
    SYSTEM_VARIABLES_ADMIN=720
    TABLE_ENCRYPTION_ADMIN=721
    VERSION_TOKEN_ADMIN=722
    XA_RECOVER_ADMIN=723
    ARMSCII8=724
    ASCII=725
    BIG5=726
    CP1250=727
    CP1251=728
    CP1256=729
    CP1257=730
    CP850=731
    CP852=732
    CP866=733
    CP932=734
    DEC8=735
    EUCJPMS=736
    EUCKR=737
    GB2312=738
    GBK=739
    GEOSTD8=740
    GREEK=741
    HEBREW=742
    HP8=743
    KEYBCS2=744
    KOI8R=745
    KOI8U=746
    LATIN1=747
    LATIN2=748
    LATIN5=749
    LATIN7=750
    MACCE=751
    MACROMAN=752
    SJIS=753
    SWE7=754
    TIS620=755
    UCS2=756
    UJIS=757
    UTF16=758
    UTF16LE=759
    UTF32=760
    UTF8=761
    UTF8MB3=762
    UTF8MB4=763
    ARCHIVE=764
    BLACKHOLE=765
    CSV=766
    FEDERATED=767
    INNODB=768
    MEMORY=769
    MRG_MYISAM=770
    MYISAM=771
    NDB=772
    NDBCLUSTER=773
    PERFORMANCE_SCHEMA=774
    TOKUDB=775
    REPEATABLE=776
    COMMITTED=777
    UNCOMMITTED=778
    SERIALIZABLE=779
    GEOMETRYCOLLECTION=780
    GEOMCOLLECTION=781
    GEOMETRY=782
    LINESTRING=783
    MULTILINESTRING=784
    MULTIPOINT=785
    MULTIPOLYGON=786
    POINT=787
    POLYGON=788
    ABS=789
    ACOS=790
    ADDDATE=791
    ADDTIME=792
    AES_DECRYPT=793
    AES_ENCRYPT=794
    AREA=795
    ASBINARY=796
    ASIN=797
    ASTEXT=798
    ASWKB=799
    ASWKT=800
    ASYMMETRIC_DECRYPT=801
    ASYMMETRIC_DERIVE=802
    ASYMMETRIC_ENCRYPT=803
    ASYMMETRIC_SIGN=804
    ASYMMETRIC_VERIFY=805
    ATAN=806
    ATAN2=807
    BENCHMARK=808
    BIN=809
    BIT_COUNT=810
    BIT_LENGTH=811
    BUFFER=812
    CATALOG_NAME=813
    CEIL=814
    CEILING=815
    CENTROID=816
    CHARACTER_LENGTH=817
    CHARSET=818
    CHAR_LENGTH=819
    COERCIBILITY=820
    COLLATION=821
    COMPRESS=822
    CONCAT=823
    CONCAT_WS=824
    CONNECTION_ID=825
    CONV=826
    CONVERT_TZ=827
    COS=828
    COT=829
    CRC32=830
    CREATE_ASYMMETRIC_PRIV_KEY=831
    CREATE_ASYMMETRIC_PUB_KEY=832
    CREATE_DH_PARAMETERS=833
    CREATE_DIGEST=834
    CROSSES=835
    DATEDIFF=836
    DATE_FORMAT=837
    DAYNAME=838
    DAYOFMONTH=839
    DAYOFWEEK=840
    DAYOFYEAR=841
    DECODE=842
    DEGREES=843
    DES_DECRYPT=844
    DES_ENCRYPT=845
    DIMENSION=846
    DISJOINT=847
    ELT=848
    ENCODE=849
    ENCRYPT=850
    ENDPOINT=851
    ENVELOPE=852
    EQUALS=853
    EXP=854
    EXPORT_SET=855
    EXTERIORRING=856
    EXTRACTVALUE=857
    FIELD=858
    FIND_IN_SET=859
    FLOOR=860
    FORMAT=861
    FOUND_ROWS=862
    FROM_BASE64=863
    FROM_DAYS=864
    FROM_UNIXTIME=865
    GEOMCOLLFROMTEXT=866
    GEOMCOLLFROMWKB=867
    GEOMETRYCOLLECTIONFROMTEXT=868
    GEOMETRYCOLLECTIONFROMWKB=869
    GEOMETRYFROMTEXT=870
    GEOMETRYFROMWKB=871
    GEOMETRYN=872
    GEOMETRYTYPE=873
    GEOMFROMTEXT=874
    GEOMFROMWKB=875
    GET_FORMAT=876
    GET_LOCK=877
    GLENGTH=878
    GREATEST=879
    GTID_SUBSET=880
    GTID_SUBTRACT=881
    HEX=882
    IFNULL=883
    INET6_ATON=884
    INET6_NTOA=885
    INET_ATON=886
    INET_NTOA=887
    INSTR=888
    INTERIORRINGN=889
    INTERSECTS=890
    ISCLOSED=891
    ISEMPTY=892
    ISNULL=893
    ISSIMPLE=894
    IS_FREE_LOCK=895
    IS_IPV4=896
    IS_IPV4_COMPAT=897
    IS_IPV4_MAPPED=898
    IS_IPV6=899
    IS_USED_LOCK=900
    LAST_INSERT_ID=901
    LCASE=902
    LEAST=903
    LENGTH=904
    LINEFROMTEXT=905
    LINEFROMWKB=906
    LINESTRINGFROMTEXT=907
    LINESTRINGFROMWKB=908
    LN=909
    LOAD_FILE=910
    LOCATE=911
    LOG=912
    LOG10=913
    LOG2=914
    LOWER=915
    LPAD=916
    LTRIM=917
    MAKEDATE=918
    MAKETIME=919
    MAKE_SET=920
    MASTER_POS_WAIT=921
    MBRCONTAINS=922
    MBRDISJOINT=923
    MBREQUAL=924
    MBRINTERSECTS=925
    MBROVERLAPS=926
    MBRTOUCHES=927
    MBRWITHIN=928
    MD5=929
    MLINEFROMTEXT=930
    MLINEFROMWKB=931
    MONTHNAME=932
    MPOINTFROMTEXT=933
    MPOINTFROMWKB=934
    MPOLYFROMTEXT=935
    MPOLYFROMWKB=936
    MULTILINESTRINGFROMTEXT=937
    MULTILINESTRINGFROMWKB=938
    MULTIPOINTFROMTEXT=939
    MULTIPOINTFROMWKB=940
    MULTIPOLYGONFROMTEXT=941
    MULTIPOLYGONFROMWKB=942
    NAME_CONST=943
    NULLIF=944
    NUMGEOMETRIES=945
    NUMINTERIORRINGS=946
    NUMPOINTS=947
    OCT=948
    OCTET_LENGTH=949
    ORD=950
    OVERLAPS=951
    PERIOD_ADD=952
    PERIOD_DIFF=953
    PI=954
    POINTFROMTEXT=955
    POINTFROMWKB=956
    POINTN=957
    POLYFROMTEXT=958
    POLYFROMWKB=959
    POLYGONFROMTEXT=960
    POLYGONFROMWKB=961
    POW=962
    POWER=963
    QUOTE=964
    RADIANS=965
    RAND=966
    RANDOM_BYTES=967
    RELEASE_LOCK=968
    REVERSE=969
    ROUND=970
    ROW_COUNT=971
    RPAD=972
    RTRIM=973
    SEC_TO_TIME=974
    SESSION_USER=975
    SHA=976
    SHA1=977
    SHA2=978
    SCHEMA_NAME=979
    SIGN=980
    SIN=981
    SLEEP=982
    SOUNDEX=983
    SQL_THREAD_WAIT_AFTER_GTIDS=984
    SQRT=985
    SRID=986
    STARTPOINT=987
    STRCMP=988
    STR_TO_DATE=989
    ST_AREA=990
    ST_ASBINARY=991
    ST_ASTEXT=992
    ST_ASWKB=993
    ST_ASWKT=994
    ST_BUFFER=995
    ST_CENTROID=996
    ST_CONTAINS=997
    ST_CROSSES=998
    ST_DIFFERENCE=999
    ST_DIMENSION=1000
    ST_DISJOINT=1001
    ST_DISTANCE=1002
    ST_ENDPOINT=1003
    ST_ENVELOPE=1004
    ST_EQUALS=1005
    ST_EXTERIORRING=1006
    ST_GEOMCOLLFROMTEXT=1007
    ST_GEOMCOLLFROMTXT=1008
    ST_GEOMCOLLFROMWKB=1009
    ST_GEOMETRYCOLLECTIONFROMTEXT=1010
    ST_GEOMETRYCOLLECTIONFROMWKB=1011
    ST_GEOMETRYFROMTEXT=1012
    ST_GEOMETRYFROMWKB=1013
    ST_GEOMETRYN=1014
    ST_GEOMETRYTYPE=1015
    ST_GEOMFROMTEXT=1016
    ST_GEOMFROMWKB=1017
    ST_INTERIORRINGN=1018
    ST_INTERSECTION=1019
    ST_INTERSECTS=1020
    ST_ISCLOSED=1021
    ST_ISEMPTY=1022
    ST_ISSIMPLE=1023
    ST_LINEFROMTEXT=1024
    ST_LINEFROMWKB=1025
    ST_LINESTRINGFROMTEXT=1026
    ST_LINESTRINGFROMWKB=1027
    ST_NUMGEOMETRIES=1028
    ST_NUMINTERIORRING=1029
    ST_NUMINTERIORRINGS=1030
    ST_NUMPOINTS=1031
    ST_OVERLAPS=1032
    ST_POINTFROMTEXT=1033
    ST_POINTFROMWKB=1034
    ST_POINTN=1035
    ST_POLYFROMTEXT=1036
    ST_POLYFROMWKB=1037
    ST_POLYGONFROMTEXT=1038
    ST_POLYGONFROMWKB=1039
    ST_SRID=1040
    ST_STARTPOINT=1041
    ST_SYMDIFFERENCE=1042
    ST_TOUCHES=1043
    ST_UNION=1044
    ST_WITHIN=1045
    ST_X=1046
    ST_Y=1047
    SUBDATE=1048
    SUBSTRING_INDEX=1049
    SUBTIME=1050
    SYSTEM_USER=1051
    TAN=1052
    TIMEDIFF=1053
    TIMESTAMPADD=1054
    TIMESTAMPDIFF=1055
    TIME_FORMAT=1056
    TIME_TO_SEC=1057
    TOUCHES=1058
    TO_BASE64=1059
    TO_DAYS=1060
    TO_SECONDS=1061
    UCASE=1062
    UNCOMPRESS=1063
    UNCOMPRESSED_LENGTH=1064
    UNHEX=1065
    UNIX_TIMESTAMP=1066
    UPDATEXML=1067
    UPPER=1068
    UUID=1069
    UUID_SHORT=1070
    VALIDATE_PASSWORD_STRENGTH=1071
    VERSION=1072
    WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS=1073
    WEEKDAY=1074
    WEEKOFYEAR=1075
    WEIGHT_STRING=1076
    WITHIN=1077
    YEARWEEK=1078
    Y_FUNCTION=1079
    X_FUNCTION=1080
    START_NATIONAL_STRING_LITERAL=1081
    STRING_LITERAL=1082
    DECIMAL_LITERAL=1083
    HEXADECIMAL_LITERAL=1084
    REAL_LITERAL=1085
    NULL_SPEC_LITERAL=1086
    BIT_STRING=1087
    DOT_ID=1088
    ID=1089
    REVERSE_QUOTE_ID=1090
    ERROR_RECONGNIGION=1091
    OPTIONAL=1092

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MySqlBaseParser.EOF, 0)

        def sqlStatements(self):
            return self.getTypedRuleContext(MySqlBaseParser.SqlStatementsContext,0)


        def MINUSMINUS(self):
            return self.getToken(MySqlBaseParser.MINUSMINUS, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = MySqlBaseParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.SEMI or _la==MySqlBaseParser.DELETE or _la==MySqlBaseParser.INSERT or _la==MySqlBaseParser.SELECT or _la==MySqlBaseParser.UPDATE:
                self.state = 94
                self.sqlStatements()


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.MINUSMINUS:
                self.state = 97
                self.match(MySqlBaseParser.MINUSMINUS)


            self.state = 100
            self.match(MySqlBaseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sqlStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.SqlStatementContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.SqlStatementContext,i)


        def emptyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.EmptyStatementContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.EmptyStatementContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.SEMI)
            else:
                return self.getToken(MySqlBaseParser.SEMI, i)

        def MINUSMINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.MINUSMINUS)
            else:
                return self.getToken(MySqlBaseParser.MINUSMINUS, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_sqlStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlStatements" ):
                listener.enterSqlStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlStatements" ):
                listener.exitSqlStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlStatements" ):
                return visitor.visitSqlStatements(self)
            else:
                return visitor.visitChildren(self)




    def sqlStatements(self):

        localctx = MySqlBaseParser.SqlStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sqlStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 110
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MySqlBaseParser.DELETE, MySqlBaseParser.INSERT, MySqlBaseParser.SELECT, MySqlBaseParser.UPDATE]:
                        self.state = 102
                        self.sqlStatement()
                        self.state = 104
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MySqlBaseParser.MINUSMINUS:
                            self.state = 103
                            self.match(MySqlBaseParser.MINUSMINUS)


                        self.state = 107
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                        if la_ == 1:
                            self.state = 106
                            self.match(MySqlBaseParser.SEMI)


                        pass
                    elif token in [MySqlBaseParser.SEMI]:
                        self.state = 109
                        self.emptyStatement()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.DELETE, MySqlBaseParser.INSERT, MySqlBaseParser.SELECT, MySqlBaseParser.UPDATE]:
                self.state = 115
                self.sqlStatement()
                self.state = 120
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 117
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MySqlBaseParser.MINUSMINUS:
                        self.state = 116
                        self.match(MySqlBaseParser.MINUSMINUS)


                    self.state = 119
                    self.match(MySqlBaseParser.SEMI)


                pass
            elif token in [MySqlBaseParser.SEMI]:
                self.state = 122
                self.emptyStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dmlStatement(self):
            return self.getTypedRuleContext(MySqlBaseParser.DmlStatementContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_sqlStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlStatement" ):
                listener.enterSqlStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlStatement" ):
                listener.exitSqlStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlStatement" ):
                return visitor.visitSqlStatement(self)
            else:
                return visitor.visitChildren(self)




    def sqlStatement(self):

        localctx = MySqlBaseParser.SqlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sqlStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.dmlStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MySqlBaseParser.SEMI, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)




    def emptyStatement(self):

        localctx = MySqlBaseParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MySqlBaseParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DmlStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectStatement(self):
            return self.getTypedRuleContext(MySqlBaseParser.SelectStatementContext,0)


        def insertStatement(self):
            return self.getTypedRuleContext(MySqlBaseParser.InsertStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(MySqlBaseParser.UpdateStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(MySqlBaseParser.DeleteStatementContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_dmlStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDmlStatement" ):
                listener.enterDmlStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDmlStatement" ):
                listener.exitDmlStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDmlStatement" ):
                return visitor.visitDmlStatement(self)
            else:
                return visitor.visitChildren(self)




    def dmlStatement(self):

        localctx = MySqlBaseParser.DmlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dmlStatement)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.SELECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.selectStatement()
                pass
            elif token in [MySqlBaseParser.INSERT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.insertStatement()
                pass
            elif token in [MySqlBaseParser.UPDATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.updateStatement()
                pass
            elif token in [MySqlBaseParser.DELETE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.deleteStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MySqlBaseParser.SELECT, 0)

        def selectElements(self):
            return self.getTypedRuleContext(MySqlBaseParser.SelectElementsContext,0)


        def FROM(self):
            return self.getToken(MySqlBaseParser.FROM, 0)

        def tableSource(self):
            return self.getTypedRuleContext(MySqlBaseParser.TableSourceContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.WhereClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.OrderByClauseContext,0)


        def limitClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.LimitClauseContext,0)


        def lockClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.LockClauseContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_selectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStatement" ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStatement" ):
                listener.exitSelectStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStatement" ):
                return visitor.visitSelectStatement(self)
            else:
                return visitor.visitChildren(self)




    def selectStatement(self):

        localctx = MySqlBaseParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_selectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MySqlBaseParser.SELECT)
            self.state = 136
            self.selectElements()
            self.state = 137
            self.match(MySqlBaseParser.FROM)
            self.state = 138
            self.tableSource()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.WHERE:
                self.state = 139
                self.whereClause()


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.ORDER:
                self.state = 142
                self.orderByClause()


            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.LIMIT:
                self.state = 145
                self.limitClause()


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.FOR or _la==MySqlBaseParser.LOCK:
                self.state = 148
                self.lockClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(MySqlBaseParser.INSERT, 0)

        def INTO(self):
            return self.getToken(MySqlBaseParser.INTO, 0)

        def tableSource(self):
            return self.getTypedRuleContext(MySqlBaseParser.TableSourceContext,0)


        def insertStatementValue(self):
            return self.getTypedRuleContext(MySqlBaseParser.InsertStatementValueContext,0)


        def VALUE(self):
            return self.getToken(MySqlBaseParser.VALUE, 0)

        def VALUES(self):
            return self.getToken(MySqlBaseParser.VALUES, 0)

        def IGNORE(self):
            return self.getToken(MySqlBaseParser.IGNORE, 0)

        def LR_BRACKET(self):
            return self.getToken(MySqlBaseParser.LR_BRACKET, 0)

        def uidList(self):
            return self.getTypedRuleContext(MySqlBaseParser.UidListContext,0)


        def RR_BRACKET(self):
            return self.getToken(MySqlBaseParser.RR_BRACKET, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_insertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStatement" ):
                listener.enterInsertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStatement" ):
                listener.exitInsertStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStatement" ):
                return visitor.visitInsertStatement(self)
            else:
                return visitor.visitChildren(self)




    def insertStatement(self):

        localctx = MySqlBaseParser.InsertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_insertStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MySqlBaseParser.INSERT)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.IGNORE:
                self.state = 152
                self.match(MySqlBaseParser.IGNORE)


            self.state = 155
            self.match(MySqlBaseParser.INTO)
            self.state = 156
            self.tableSource()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.LR_BRACKET:
                self.state = 157
                self.match(MySqlBaseParser.LR_BRACKET)
                self.state = 158
                self.uidList()
                self.state = 159
                self.match(MySqlBaseParser.RR_BRACKET)


            self.state = 163
            _la = self._input.LA(1)
            if not(_la==MySqlBaseParser.VALUES or _la==MySqlBaseParser.VALUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self.insertStatementValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(MySqlBaseParser.UPDATE, 0)

        def tableSource(self):
            return self.getTypedRuleContext(MySqlBaseParser.TableSourceContext,0)


        def SET(self):
            return self.getToken(MySqlBaseParser.SET, 0)

        def updatedElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.UpdatedElementContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.UpdatedElementContext,i)


        def IGNORE(self):
            return self.getToken(MySqlBaseParser.IGNORE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.COMMA)
            else:
                return self.getToken(MySqlBaseParser.COMMA, i)

        def whereClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.WhereClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.OrderByClauseContext,0)


        def limitClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.LimitClauseContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_updateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStatement" ):
                listener.enterUpdateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStatement" ):
                listener.exitUpdateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStatement" ):
                return visitor.visitUpdateStatement(self)
            else:
                return visitor.visitChildren(self)




    def updateStatement(self):

        localctx = MySqlBaseParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_updateStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MySqlBaseParser.UPDATE)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.IGNORE:
                self.state = 167
                self.match(MySqlBaseParser.IGNORE)


            self.state = 170
            self.tableSource()
            self.state = 171
            self.match(MySqlBaseParser.SET)
            self.state = 172
            self.updatedElement()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlBaseParser.COMMA:
                self.state = 173
                self.match(MySqlBaseParser.COMMA)
                self.state = 174
                self.updatedElement()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.WHERE:
                self.state = 180
                self.whereClause()


            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.ORDER:
                self.state = 183
                self.orderByClause()


            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.LIMIT:
                self.state = 186
                self.limitClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(MySqlBaseParser.DELETE, 0)

        def FROM(self):
            return self.getToken(MySqlBaseParser.FROM, 0)

        def tableSource(self):
            return self.getTypedRuleContext(MySqlBaseParser.TableSourceContext,0)


        def IGNORE(self):
            return self.getToken(MySqlBaseParser.IGNORE, 0)

        def tableAlias(self):
            return self.getTypedRuleContext(MySqlBaseParser.TableAliasContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.WhereClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(MySqlBaseParser.OrderByClauseContext,0)


        def LIMIT(self):
            return self.getToken(MySqlBaseParser.LIMIT, 0)

        def decimalLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.DecimalLiteralContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_deleteStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStatement" ):
                listener.enterDeleteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStatement" ):
                listener.exitDeleteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStatement" ):
                return visitor.visitDeleteStatement(self)
            else:
                return visitor.visitChildren(self)




    def deleteStatement(self):

        localctx = MySqlBaseParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_deleteStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MySqlBaseParser.DELETE)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.IGNORE:
                self.state = 190
                self.match(MySqlBaseParser.IGNORE)


            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (MySqlBaseParser.CURRENT - 76)) | (1 << (MySqlBaseParser.DIAGNOSTICS - 76)) | (1 << (MySqlBaseParser.GROUP - 76)))) != 0) or ((((_la - 150)) & ~0x3f) == 0 and ((1 << (_la - 150)) & ((1 << (MySqlBaseParser.NUMBER - 150)) | (1 << (MySqlBaseParser.ORDER - 150)) | (1 << (MySqlBaseParser.STACKED - 150)))) != 0) or ((((_la - 266)) & ~0x3f) == 0 and ((1 << (_la - 266)) & ((1 << (MySqlBaseParser.SERIAL - 266)) | (1 << (MySqlBaseParser.AVG - 266)) | (1 << (MySqlBaseParser.BIT_AND - 266)) | (1 << (MySqlBaseParser.BIT_OR - 266)) | (1 << (MySqlBaseParser.BIT_XOR - 266)) | (1 << (MySqlBaseParser.COUNT - 266)) | (1 << (MySqlBaseParser.GROUP_CONCAT - 266)) | (1 << (MySqlBaseParser.MAX - 266)) | (1 << (MySqlBaseParser.MIN - 266)) | (1 << (MySqlBaseParser.STD - 266)) | (1 << (MySqlBaseParser.STDDEV - 266)) | (1 << (MySqlBaseParser.STDDEV_POP - 266)) | (1 << (MySqlBaseParser.STDDEV_SAMP - 266)) | (1 << (MySqlBaseParser.SUM - 266)) | (1 << (MySqlBaseParser.VAR_POP - 266)) | (1 << (MySqlBaseParser.VAR_SAMP - 266)) | (1 << (MySqlBaseParser.VARIANCE - 266)))) != 0) or ((((_la - 345)) & ~0x3f) == 0 and ((1 << (_la - 345)) & ((1 << (MySqlBaseParser.ACCOUNT - 345)) | (1 << (MySqlBaseParser.ACTION - 345)) | (1 << (MySqlBaseParser.AFTER - 345)) | (1 << (MySqlBaseParser.AGGREGATE - 345)) | (1 << (MySqlBaseParser.ALGORITHM - 345)) | (1 << (MySqlBaseParser.ANY - 345)) | (1 << (MySqlBaseParser.AT - 345)) | (1 << (MySqlBaseParser.AUTHORS - 345)) | (1 << (MySqlBaseParser.AUTOCOMMIT - 345)) | (1 << (MySqlBaseParser.AUTOEXTEND_SIZE - 345)) | (1 << (MySqlBaseParser.AUTO_INCREMENT - 345)) | (1 << (MySqlBaseParser.AVG_ROW_LENGTH - 345)) | (1 << (MySqlBaseParser.BEGIN - 345)) | (1 << (MySqlBaseParser.BINLOG - 345)) | (1 << (MySqlBaseParser.BIT - 345)) | (1 << (MySqlBaseParser.BLOCK - 345)) | (1 << (MySqlBaseParser.BOOL - 345)) | (1 << (MySqlBaseParser.BOOLEAN - 345)) | (1 << (MySqlBaseParser.BTREE - 345)) | (1 << (MySqlBaseParser.CACHE - 345)) | (1 << (MySqlBaseParser.CASCADED - 345)) | (1 << (MySqlBaseParser.CHAIN - 345)) | (1 << (MySqlBaseParser.CHANGED - 345)) | (1 << (MySqlBaseParser.CHANNEL - 345)) | (1 << (MySqlBaseParser.CHECKSUM - 345)) | (1 << (MySqlBaseParser.PAGE_CHECKSUM - 345)) | (1 << (MySqlBaseParser.CIPHER - 345)) | (1 << (MySqlBaseParser.CLASS_ORIGIN - 345)) | (1 << (MySqlBaseParser.CLIENT - 345)) | (1 << (MySqlBaseParser.CLOSE - 345)) | (1 << (MySqlBaseParser.COALESCE - 345)) | (1 << (MySqlBaseParser.CODE - 345)) | (1 << (MySqlBaseParser.COLUMNS - 345)) | (1 << (MySqlBaseParser.COLUMN_FORMAT - 345)) | (1 << (MySqlBaseParser.COLUMN_NAME - 345)) | (1 << (MySqlBaseParser.COMMENT - 345)) | (1 << (MySqlBaseParser.COMMIT - 345)) | (1 << (MySqlBaseParser.COMPACT - 345)) | (1 << (MySqlBaseParser.COMPLETION - 345)) | (1 << (MySqlBaseParser.COMPRESSED - 345)) | (1 << (MySqlBaseParser.COMPRESSION - 345)) | (1 << (MySqlBaseParser.CONCURRENT - 345)) | (1 << (MySqlBaseParser.CONNECT - 345)) | (1 << (MySqlBaseParser.CONNECTION - 345)) | (1 << (MySqlBaseParser.CONSISTENT - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_CATALOG - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_SCHEMA - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_NAME - 345)) | (1 << (MySqlBaseParser.CONTAINS - 345)) | (1 << (MySqlBaseParser.CONTEXT - 345)) | (1 << (MySqlBaseParser.CONTRIBUTORS - 345)) | (1 << (MySqlBaseParser.COPY - 345)) | (1 << (MySqlBaseParser.CPU - 345)) | (1 << (MySqlBaseParser.CURSOR_NAME - 345)) | (1 << (MySqlBaseParser.DATA - 345)) | (1 << (MySqlBaseParser.DATAFILE - 345)) | (1 << (MySqlBaseParser.DEALLOCATE - 345)) | (1 << (MySqlBaseParser.DEFAULT_AUTH - 345)) | (1 << (MySqlBaseParser.DEFINER - 345)) | (1 << (MySqlBaseParser.DELAY_KEY_WRITE - 345)) | (1 << (MySqlBaseParser.DES_KEY_FILE - 345)) | (1 << (MySqlBaseParser.DIRECTORY - 345)) | (1 << (MySqlBaseParser.DISABLE - 345)) | (1 << (MySqlBaseParser.DISCARD - 345)))) != 0) or ((((_la - 409)) & ~0x3f) == 0 and ((1 << (_la - 409)) & ((1 << (MySqlBaseParser.DISK - 409)) | (1 << (MySqlBaseParser.DO - 409)) | (1 << (MySqlBaseParser.DUMPFILE - 409)) | (1 << (MySqlBaseParser.DUPLICATE - 409)) | (1 << (MySqlBaseParser.DYNAMIC - 409)) | (1 << (MySqlBaseParser.ENABLE - 409)) | (1 << (MySqlBaseParser.ENCRYPTION - 409)) | (1 << (MySqlBaseParser.END - 409)) | (1 << (MySqlBaseParser.ENDS - 409)) | (1 << (MySqlBaseParser.ENGINE - 409)) | (1 << (MySqlBaseParser.ENGINES - 409)) | (1 << (MySqlBaseParser.ERROR - 409)) | (1 << (MySqlBaseParser.ERRORS - 409)) | (1 << (MySqlBaseParser.ESCAPE - 409)) | (1 << (MySqlBaseParser.EVEN - 409)) | (1 << (MySqlBaseParser.EVENT - 409)) | (1 << (MySqlBaseParser.EVENTS - 409)) | (1 << (MySqlBaseParser.EVERY - 409)) | (1 << (MySqlBaseParser.EXCHANGE - 409)) | (1 << (MySqlBaseParser.EXCLUSIVE - 409)) | (1 << (MySqlBaseParser.EXPIRE - 409)) | (1 << (MySqlBaseParser.EXPORT - 409)) | (1 << (MySqlBaseParser.EXTENDED - 409)) | (1 << (MySqlBaseParser.EXTENT_SIZE - 409)) | (1 << (MySqlBaseParser.FAST - 409)) | (1 << (MySqlBaseParser.FAULTS - 409)) | (1 << (MySqlBaseParser.FIELDS - 409)) | (1 << (MySqlBaseParser.FILE_BLOCK_SIZE - 409)) | (1 << (MySqlBaseParser.FILTER - 409)) | (1 << (MySqlBaseParser.FIRST - 409)) | (1 << (MySqlBaseParser.FIXED - 409)) | (1 << (MySqlBaseParser.FLUSH - 409)) | (1 << (MySqlBaseParser.FOLLOWS - 409)) | (1 << (MySqlBaseParser.FOUND - 409)) | (1 << (MySqlBaseParser.FULL - 409)) | (1 << (MySqlBaseParser.FUNCTION - 409)) | (1 << (MySqlBaseParser.GENERAL - 409)) | (1 << (MySqlBaseParser.GLOBAL - 409)) | (1 << (MySqlBaseParser.GRANTS - 409)) | (1 << (MySqlBaseParser.GROUP_REPLICATION - 409)) | (1 << (MySqlBaseParser.HANDLER - 409)) | (1 << (MySqlBaseParser.HASH - 409)) | (1 << (MySqlBaseParser.HELP - 409)) | (1 << (MySqlBaseParser.HOST - 409)) | (1 << (MySqlBaseParser.HOSTS - 409)) | (1 << (MySqlBaseParser.IDENTIFIED - 409)) | (1 << (MySqlBaseParser.IGNORE_SERVER_IDS - 409)) | (1 << (MySqlBaseParser.IMPORT - 409)) | (1 << (MySqlBaseParser.INDEXES - 409)) | (1 << (MySqlBaseParser.INITIAL_SIZE - 409)) | (1 << (MySqlBaseParser.INPLACE - 409)) | (1 << (MySqlBaseParser.INSERT_METHOD - 409)) | (1 << (MySqlBaseParser.INSTALL - 409)) | (1 << (MySqlBaseParser.INSTANCE - 409)) | (1 << (MySqlBaseParser.INVOKER - 409)) | (1 << (MySqlBaseParser.IO - 409)) | (1 << (MySqlBaseParser.IO_THREAD - 409)) | (1 << (MySqlBaseParser.IPC - 409)) | (1 << (MySqlBaseParser.ISOLATION - 409)) | (1 << (MySqlBaseParser.ISSUER - 409)) | (1 << (MySqlBaseParser.JSON - 409)) | (1 << (MySqlBaseParser.KEY_BLOCK_SIZE - 409)) | (1 << (MySqlBaseParser.LANGUAGE - 409)))) != 0) or ((((_la - 473)) & ~0x3f) == 0 and ((1 << (_la - 473)) & ((1 << (MySqlBaseParser.LAST - 473)) | (1 << (MySqlBaseParser.LEAVES - 473)) | (1 << (MySqlBaseParser.LESS - 473)) | (1 << (MySqlBaseParser.LEVEL - 473)) | (1 << (MySqlBaseParser.LIST - 473)) | (1 << (MySqlBaseParser.LOCAL - 473)) | (1 << (MySqlBaseParser.LOGFILE - 473)) | (1 << (MySqlBaseParser.LOGS - 473)) | (1 << (MySqlBaseParser.MASTER - 473)) | (1 << (MySqlBaseParser.MASTER_AUTO_POSITION - 473)) | (1 << (MySqlBaseParser.MASTER_CONNECT_RETRY - 473)) | (1 << (MySqlBaseParser.MASTER_DELAY - 473)) | (1 << (MySqlBaseParser.MASTER_HEARTBEAT_PERIOD - 473)) | (1 << (MySqlBaseParser.MASTER_HOST - 473)) | (1 << (MySqlBaseParser.MASTER_LOG_FILE - 473)) | (1 << (MySqlBaseParser.MASTER_LOG_POS - 473)) | (1 << (MySqlBaseParser.MASTER_PASSWORD - 473)) | (1 << (MySqlBaseParser.MASTER_PORT - 473)) | (1 << (MySqlBaseParser.MASTER_RETRY_COUNT - 473)) | (1 << (MySqlBaseParser.MASTER_SSL - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CA - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CAPATH - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CERT - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CIPHER - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CRL - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CRLPATH - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_KEY - 473)) | (1 << (MySqlBaseParser.MASTER_TLS_VERSION - 473)) | (1 << (MySqlBaseParser.MASTER_USER - 473)) | (1 << (MySqlBaseParser.MAX_CONNECTIONS_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_QUERIES_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_ROWS - 473)) | (1 << (MySqlBaseParser.MAX_SIZE - 473)) | (1 << (MySqlBaseParser.MAX_UPDATES_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_USER_CONNECTIONS - 473)) | (1 << (MySqlBaseParser.MEDIUM - 473)) | (1 << (MySqlBaseParser.MEMBER - 473)) | (1 << (MySqlBaseParser.MERGE - 473)) | (1 << (MySqlBaseParser.MESSAGE_TEXT - 473)) | (1 << (MySqlBaseParser.MID - 473)) | (1 << (MySqlBaseParser.MIGRATE - 473)) | (1 << (MySqlBaseParser.MIN_ROWS - 473)) | (1 << (MySqlBaseParser.MODE - 473)) | (1 << (MySqlBaseParser.MODIFY - 473)) | (1 << (MySqlBaseParser.MUTEX - 473)) | (1 << (MySqlBaseParser.MYSQL - 473)) | (1 << (MySqlBaseParser.MYSQL_ERRNO - 473)) | (1 << (MySqlBaseParser.NAME - 473)) | (1 << (MySqlBaseParser.NAMES - 473)) | (1 << (MySqlBaseParser.NCHAR - 473)) | (1 << (MySqlBaseParser.NEVER - 473)) | (1 << (MySqlBaseParser.NEXT - 473)) | (1 << (MySqlBaseParser.NO - 473)) | (1 << (MySqlBaseParser.NODEGROUP - 473)) | (1 << (MySqlBaseParser.NONE - 473)) | (1 << (MySqlBaseParser.ODBC - 473)) | (1 << (MySqlBaseParser.OFFLINE - 473)) | (1 << (MySqlBaseParser.OFFSET - 473)) | (1 << (MySqlBaseParser.OF - 473)) | (1 << (MySqlBaseParser.OJ - 473)) | (1 << (MySqlBaseParser.OLD_PASSWORD - 473)) | (1 << (MySqlBaseParser.ONE - 473)) | (1 << (MySqlBaseParser.ONLINE - 473)) | (1 << (MySqlBaseParser.ONLY - 473)))) != 0) or ((((_la - 537)) & ~0x3f) == 0 and ((1 << (_la - 537)) & ((1 << (MySqlBaseParser.OPEN - 537)) | (1 << (MySqlBaseParser.OPTIMIZER_COSTS - 537)) | (1 << (MySqlBaseParser.OPTIONS - 537)) | (1 << (MySqlBaseParser.OWNER - 537)) | (1 << (MySqlBaseParser.PACK_KEYS - 537)) | (1 << (MySqlBaseParser.PAGE - 537)) | (1 << (MySqlBaseParser.PARSER - 537)) | (1 << (MySqlBaseParser.PARTIAL - 537)) | (1 << (MySqlBaseParser.PARTITIONING - 537)) | (1 << (MySqlBaseParser.PARTITIONS - 537)) | (1 << (MySqlBaseParser.PASSWORD - 537)) | (1 << (MySqlBaseParser.PHASE - 537)) | (1 << (MySqlBaseParser.PLUGIN - 537)) | (1 << (MySqlBaseParser.PLUGIN_DIR - 537)) | (1 << (MySqlBaseParser.PLUGINS - 537)) | (1 << (MySqlBaseParser.PORT - 537)) | (1 << (MySqlBaseParser.PRECEDES - 537)) | (1 << (MySqlBaseParser.PREPARE - 537)) | (1 << (MySqlBaseParser.PRESERVE - 537)) | (1 << (MySqlBaseParser.PREV - 537)) | (1 << (MySqlBaseParser.PROCESSLIST - 537)) | (1 << (MySqlBaseParser.PROFILE - 537)) | (1 << (MySqlBaseParser.PROFILES - 537)) | (1 << (MySqlBaseParser.PROXY - 537)) | (1 << (MySqlBaseParser.QUERY - 537)) | (1 << (MySqlBaseParser.QUICK - 537)) | (1 << (MySqlBaseParser.REBUILD - 537)) | (1 << (MySqlBaseParser.RECOVER - 537)) | (1 << (MySqlBaseParser.REDO_BUFFER_SIZE - 537)) | (1 << (MySqlBaseParser.REDUNDANT - 537)) | (1 << (MySqlBaseParser.RELAY - 537)) | (1 << (MySqlBaseParser.RELAY_LOG_FILE - 537)) | (1 << (MySqlBaseParser.RELAY_LOG_POS - 537)) | (1 << (MySqlBaseParser.RELAYLOG - 537)) | (1 << (MySqlBaseParser.REMOVE - 537)) | (1 << (MySqlBaseParser.REORGANIZE - 537)) | (1 << (MySqlBaseParser.REPAIR - 537)) | (1 << (MySqlBaseParser.REPLICATE_DO_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_DO_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_IGNORE_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_IGNORE_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_REWRITE_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_WILD_DO_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_WILD_IGNORE_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATION - 537)) | (1 << (MySqlBaseParser.RESET - 537)) | (1 << (MySqlBaseParser.RESUME - 537)) | (1 << (MySqlBaseParser.RETURNED_SQLSTATE - 537)) | (1 << (MySqlBaseParser.RETURNS - 537)) | (1 << (MySqlBaseParser.ROLE - 537)) | (1 << (MySqlBaseParser.ROLLBACK - 537)) | (1 << (MySqlBaseParser.ROLLUP - 537)) | (1 << (MySqlBaseParser.ROTATE - 537)) | (1 << (MySqlBaseParser.ROW - 537)) | (1 << (MySqlBaseParser.ROWS - 537)) | (1 << (MySqlBaseParser.ROW_FORMAT - 537)) | (1 << (MySqlBaseParser.SAVEPOINT - 537)) | (1 << (MySqlBaseParser.SCHEDULE - 537)) | (1 << (MySqlBaseParser.SECURITY - 537)) | (1 << (MySqlBaseParser.SERVER - 537)) | (1 << (MySqlBaseParser.SESSION - 537)) | (1 << (MySqlBaseParser.SHARE - 537)) | (1 << (MySqlBaseParser.SHARED - 537)))) != 0) or ((((_la - 601)) & ~0x3f) == 0 and ((1 << (_la - 601)) & ((1 << (MySqlBaseParser.SIGNED - 601)) | (1 << (MySqlBaseParser.SIMPLE - 601)) | (1 << (MySqlBaseParser.SLAVE - 601)) | (1 << (MySqlBaseParser.SLOW - 601)) | (1 << (MySqlBaseParser.SNAPSHOT - 601)) | (1 << (MySqlBaseParser.SOCKET - 601)) | (1 << (MySqlBaseParser.SOME - 601)) | (1 << (MySqlBaseParser.SONAME - 601)) | (1 << (MySqlBaseParser.SOUNDS - 601)) | (1 << (MySqlBaseParser.SOURCE - 601)) | (1 << (MySqlBaseParser.SQL_AFTER_GTIDS - 601)) | (1 << (MySqlBaseParser.SQL_AFTER_MTS_GAPS - 601)) | (1 << (MySqlBaseParser.SQL_BEFORE_GTIDS - 601)) | (1 << (MySqlBaseParser.SQL_BUFFER_RESULT - 601)) | (1 << (MySqlBaseParser.SQL_CACHE - 601)) | (1 << (MySqlBaseParser.SQL_NO_CACHE - 601)) | (1 << (MySqlBaseParser.SQL_THREAD - 601)) | (1 << (MySqlBaseParser.START - 601)) | (1 << (MySqlBaseParser.STARTS - 601)) | (1 << (MySqlBaseParser.STATS_AUTO_RECALC - 601)) | (1 << (MySqlBaseParser.STATS_PERSISTENT - 601)) | (1 << (MySqlBaseParser.STATS_SAMPLE_PAGES - 601)) | (1 << (MySqlBaseParser.STATUS - 601)) | (1 << (MySqlBaseParser.STOP - 601)) | (1 << (MySqlBaseParser.STORAGE - 601)) | (1 << (MySqlBaseParser.STRING - 601)) | (1 << (MySqlBaseParser.SUBCLASS_ORIGIN - 601)) | (1 << (MySqlBaseParser.SUBJECT - 601)) | (1 << (MySqlBaseParser.SUBPARTITION - 601)) | (1 << (MySqlBaseParser.SUBPARTITIONS - 601)) | (1 << (MySqlBaseParser.SUSPEND - 601)) | (1 << (MySqlBaseParser.SWAPS - 601)) | (1 << (MySqlBaseParser.SWITCHES - 601)) | (1 << (MySqlBaseParser.TABLE_NAME - 601)) | (1 << (MySqlBaseParser.TABLESPACE - 601)) | (1 << (MySqlBaseParser.TEMPORARY - 601)) | (1 << (MySqlBaseParser.TEMPTABLE - 601)) | (1 << (MySqlBaseParser.THAN - 601)) | (1 << (MySqlBaseParser.TRADITIONAL - 601)) | (1 << (MySqlBaseParser.TRANSACTION - 601)) | (1 << (MySqlBaseParser.TRANSACTIONAL - 601)) | (1 << (MySqlBaseParser.TRIGGERS - 601)) | (1 << (MySqlBaseParser.TRUNCATE - 601)) | (1 << (MySqlBaseParser.UNDEFINED - 601)) | (1 << (MySqlBaseParser.UNDOFILE - 601)) | (1 << (MySqlBaseParser.UNDO_BUFFER_SIZE - 601)) | (1 << (MySqlBaseParser.UNINSTALL - 601)) | (1 << (MySqlBaseParser.UNKNOWN - 601)) | (1 << (MySqlBaseParser.UNTIL - 601)) | (1 << (MySqlBaseParser.UPGRADE - 601)) | (1 << (MySqlBaseParser.USER - 601)) | (1 << (MySqlBaseParser.USE_FRM - 601)) | (1 << (MySqlBaseParser.USER_RESOURCES - 601)) | (1 << (MySqlBaseParser.VALIDATION - 601)) | (1 << (MySqlBaseParser.VALUE - 601)) | (1 << (MySqlBaseParser.VARIABLES - 601)) | (1 << (MySqlBaseParser.VIEW - 601)) | (1 << (MySqlBaseParser.WAIT - 601)) | (1 << (MySqlBaseParser.WARNINGS - 601)) | (1 << (MySqlBaseParser.WITHOUT - 601)))) != 0) or ((((_la - 665)) & ~0x3f) == 0 and ((1 << (_la - 665)) & ((1 << (MySqlBaseParser.WORK - 665)) | (1 << (MySqlBaseParser.WRAPPER - 665)) | (1 << (MySqlBaseParser.X509 - 665)) | (1 << (MySqlBaseParser.XA - 665)) | (1 << (MySqlBaseParser.XML - 665)) | (1 << (MySqlBaseParser.INTERNAL - 665)) | (1 << (MySqlBaseParser.AUDIT_ADMIN - 665)) | (1 << (MySqlBaseParser.BACKUP_ADMIN - 665)) | (1 << (MySqlBaseParser.BINLOG_ADMIN - 665)) | (1 << (MySqlBaseParser.BINLOG_ENCRYPTION_ADMIN - 665)) | (1 << (MySqlBaseParser.CLONE_ADMIN - 665)) | (1 << (MySqlBaseParser.CONNECTION_ADMIN - 665)) | (1 << (MySqlBaseParser.ENCRYPTION_KEY_ADMIN - 665)) | (1 << (MySqlBaseParser.FIREWALL_ADMIN - 665)) | (1 << (MySqlBaseParser.FIREWALL_USER - 665)) | (1 << (MySqlBaseParser.GROUP_REPLICATION_ADMIN - 665)) | (1 << (MySqlBaseParser.INNODB_REDO_LOG_ARCHIVE - 665)) | (1 << (MySqlBaseParser.NDB_STORED_USER - 665)) | (1 << (MySqlBaseParser.PERSIST_RO_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.REPLICATION_APPLIER - 665)) | (1 << (MySqlBaseParser.REPLICATION_SLAVE_ADMIN - 665)) | (1 << (MySqlBaseParser.RESOURCE_GROUP_ADMIN - 665)) | (1 << (MySqlBaseParser.RESOURCE_GROUP_USER - 665)) | (1 << (MySqlBaseParser.ROLE_ADMIN - 665)) | (1 << (MySqlBaseParser.SESSION_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.SET_USER_ID - 665)) | (1 << (MySqlBaseParser.SHOW_ROUTINE - 665)) | (1 << (MySqlBaseParser.SYSTEM_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.TABLE_ENCRYPTION_ADMIN - 665)) | (1 << (MySqlBaseParser.VERSION_TOKEN_ADMIN - 665)) | (1 << (MySqlBaseParser.XA_RECOVER_ADMIN - 665)))) != 0) or _la==MySqlBaseParser.MEMORY or _la==MySqlBaseParser.CATALOG_NAME or _la==MySqlBaseParser.SCHEMA_NAME or ((((_la - 1082)) & ~0x3f) == 0 and ((1 << (_la - 1082)) & ((1 << (MySqlBaseParser.STRING_LITERAL - 1082)) | (1 << (MySqlBaseParser.ID - 1082)) | (1 << (MySqlBaseParser.OPTIONAL - 1082)))) != 0):
                self.state = 193
                self.tableAlias()


            self.state = 196
            self.match(MySqlBaseParser.FROM)
            self.state = 197
            self.tableSource()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.WHERE:
                self.state = 198
                self.whereClause()


            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.ORDER:
                self.state = 201
                self.orderByClause()


            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.LIMIT:
                self.state = 204
                self.match(MySqlBaseParser.LIMIT)
                self.state = 205
                self.decimalLiteral()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStatementValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.LR_BRACKET)
            else:
                return self.getToken(MySqlBaseParser.LR_BRACKET, i)

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.ExpressionsContext,i)


        def RR_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.RR_BRACKET)
            else:
                return self.getToken(MySqlBaseParser.RR_BRACKET, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.COMMA)
            else:
                return self.getToken(MySqlBaseParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_insertStatementValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStatementValue" ):
                listener.enterInsertStatementValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStatementValue" ):
                listener.exitInsertStatementValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStatementValue" ):
                return visitor.visitInsertStatementValue(self)
            else:
                return visitor.visitChildren(self)




    def insertStatementValue(self):

        localctx = MySqlBaseParser.InsertStatementValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_insertStatementValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MySqlBaseParser.LR_BRACKET)
            self.state = 209
            self.expressions()
            self.state = 210
            self.match(MySqlBaseParser.RR_BRACKET)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlBaseParser.COMMA:
                self.state = 212
                self.match(MySqlBaseParser.COMMA)
                self.state = 213
                self.match(MySqlBaseParser.LR_BRACKET)
                self.state = 214
                self.expressions()
                self.state = 215
                self.match(MySqlBaseParser.RR_BRACKET)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.star = None # Token

        def selectElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.SelectElementContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.SelectElementContext,i)


        def STAR(self):
            return self.getToken(MySqlBaseParser.STAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.COMMA)
            else:
                return self.getToken(MySqlBaseParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_selectElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectElements" ):
                listener.enterSelectElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectElements" ):
                listener.exitSelectElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectElements" ):
                return visitor.visitSelectElements(self)
            else:
                return visitor.visitChildren(self)




    def selectElements(self):

        localctx = MySqlBaseParser.SelectElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_selectElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 222
                localctx.star = self.match(MySqlBaseParser.STAR)
                pass

            elif la_ == 2:
                self.state = 223
                self.selectElement()
                pass


            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlBaseParser.COMMA:
                self.state = 226
                self.match(MySqlBaseParser.COMMA)
                self.state = 227
                self.selectElement()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_selectElement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectStarElementContext(SelectElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.SelectElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fullId(self):
            return self.getTypedRuleContext(MySqlBaseParser.FullIdContext,0)

        def DOT(self):
            return self.getToken(MySqlBaseParser.DOT, 0)
        def STAR(self):
            return self.getToken(MySqlBaseParser.STAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStarElement" ):
                listener.enterSelectStarElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStarElement" ):
                listener.exitSelectStarElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStarElement" ):
                return visitor.visitSelectStarElement(self)
            else:
                return visitor.visitChildren(self)


    class SelectColumnElementContext(SelectElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.SelectElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fullColumnName(self):
            return self.getTypedRuleContext(MySqlBaseParser.FullColumnNameContext,0)

        def uid(self):
            return self.getTypedRuleContext(MySqlBaseParser.UidContext,0)

        def AS(self):
            return self.getToken(MySqlBaseParser.AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectColumnElement" ):
                listener.enterSelectColumnElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectColumnElement" ):
                listener.exitSelectColumnElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectColumnElement" ):
                return visitor.visitSelectColumnElement(self)
            else:
                return visitor.visitChildren(self)



    def selectElement(self):

        localctx = MySqlBaseParser.SelectElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_selectElement)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = MySqlBaseParser.SelectStarElementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.fullId()
                self.state = 234
                self.match(MySqlBaseParser.DOT)
                self.state = 235
                self.match(MySqlBaseParser.STAR)
                pass

            elif la_ == 2:
                localctx = MySqlBaseParser.SelectColumnElementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.fullColumnName()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & ((1 << (MySqlBaseParser.AS - 55)) | (1 << (MySqlBaseParser.CURRENT - 55)) | (1 << (MySqlBaseParser.DIAGNOSTICS - 55)) | (1 << (MySqlBaseParser.GROUP - 55)))) != 0) or ((((_la - 150)) & ~0x3f) == 0 and ((1 << (_la - 150)) & ((1 << (MySqlBaseParser.NUMBER - 150)) | (1 << (MySqlBaseParser.ORDER - 150)) | (1 << (MySqlBaseParser.STACKED - 150)))) != 0) or ((((_la - 266)) & ~0x3f) == 0 and ((1 << (_la - 266)) & ((1 << (MySqlBaseParser.SERIAL - 266)) | (1 << (MySqlBaseParser.AVG - 266)) | (1 << (MySqlBaseParser.BIT_AND - 266)) | (1 << (MySqlBaseParser.BIT_OR - 266)) | (1 << (MySqlBaseParser.BIT_XOR - 266)) | (1 << (MySqlBaseParser.COUNT - 266)) | (1 << (MySqlBaseParser.GROUP_CONCAT - 266)) | (1 << (MySqlBaseParser.MAX - 266)) | (1 << (MySqlBaseParser.MIN - 266)) | (1 << (MySqlBaseParser.STD - 266)) | (1 << (MySqlBaseParser.STDDEV - 266)) | (1 << (MySqlBaseParser.STDDEV_POP - 266)) | (1 << (MySqlBaseParser.STDDEV_SAMP - 266)) | (1 << (MySqlBaseParser.SUM - 266)) | (1 << (MySqlBaseParser.VAR_POP - 266)) | (1 << (MySqlBaseParser.VAR_SAMP - 266)) | (1 << (MySqlBaseParser.VARIANCE - 266)))) != 0) or ((((_la - 345)) & ~0x3f) == 0 and ((1 << (_la - 345)) & ((1 << (MySqlBaseParser.ACCOUNT - 345)) | (1 << (MySqlBaseParser.ACTION - 345)) | (1 << (MySqlBaseParser.AFTER - 345)) | (1 << (MySqlBaseParser.AGGREGATE - 345)) | (1 << (MySqlBaseParser.ALGORITHM - 345)) | (1 << (MySqlBaseParser.ANY - 345)) | (1 << (MySqlBaseParser.AT - 345)) | (1 << (MySqlBaseParser.AUTHORS - 345)) | (1 << (MySqlBaseParser.AUTOCOMMIT - 345)) | (1 << (MySqlBaseParser.AUTOEXTEND_SIZE - 345)) | (1 << (MySqlBaseParser.AUTO_INCREMENT - 345)) | (1 << (MySqlBaseParser.AVG_ROW_LENGTH - 345)) | (1 << (MySqlBaseParser.BEGIN - 345)) | (1 << (MySqlBaseParser.BINLOG - 345)) | (1 << (MySqlBaseParser.BIT - 345)) | (1 << (MySqlBaseParser.BLOCK - 345)) | (1 << (MySqlBaseParser.BOOL - 345)) | (1 << (MySqlBaseParser.BOOLEAN - 345)) | (1 << (MySqlBaseParser.BTREE - 345)) | (1 << (MySqlBaseParser.CACHE - 345)) | (1 << (MySqlBaseParser.CASCADED - 345)) | (1 << (MySqlBaseParser.CHAIN - 345)) | (1 << (MySqlBaseParser.CHANGED - 345)) | (1 << (MySqlBaseParser.CHANNEL - 345)) | (1 << (MySqlBaseParser.CHECKSUM - 345)) | (1 << (MySqlBaseParser.PAGE_CHECKSUM - 345)) | (1 << (MySqlBaseParser.CIPHER - 345)) | (1 << (MySqlBaseParser.CLASS_ORIGIN - 345)) | (1 << (MySqlBaseParser.CLIENT - 345)) | (1 << (MySqlBaseParser.CLOSE - 345)) | (1 << (MySqlBaseParser.COALESCE - 345)) | (1 << (MySqlBaseParser.CODE - 345)) | (1 << (MySqlBaseParser.COLUMNS - 345)) | (1 << (MySqlBaseParser.COLUMN_FORMAT - 345)) | (1 << (MySqlBaseParser.COLUMN_NAME - 345)) | (1 << (MySqlBaseParser.COMMENT - 345)) | (1 << (MySqlBaseParser.COMMIT - 345)) | (1 << (MySqlBaseParser.COMPACT - 345)) | (1 << (MySqlBaseParser.COMPLETION - 345)) | (1 << (MySqlBaseParser.COMPRESSED - 345)) | (1 << (MySqlBaseParser.COMPRESSION - 345)) | (1 << (MySqlBaseParser.CONCURRENT - 345)) | (1 << (MySqlBaseParser.CONNECT - 345)) | (1 << (MySqlBaseParser.CONNECTION - 345)) | (1 << (MySqlBaseParser.CONSISTENT - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_CATALOG - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_SCHEMA - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_NAME - 345)) | (1 << (MySqlBaseParser.CONTAINS - 345)) | (1 << (MySqlBaseParser.CONTEXT - 345)) | (1 << (MySqlBaseParser.CONTRIBUTORS - 345)) | (1 << (MySqlBaseParser.COPY - 345)) | (1 << (MySqlBaseParser.CPU - 345)) | (1 << (MySqlBaseParser.CURSOR_NAME - 345)) | (1 << (MySqlBaseParser.DATA - 345)) | (1 << (MySqlBaseParser.DATAFILE - 345)) | (1 << (MySqlBaseParser.DEALLOCATE - 345)) | (1 << (MySqlBaseParser.DEFAULT_AUTH - 345)) | (1 << (MySqlBaseParser.DEFINER - 345)) | (1 << (MySqlBaseParser.DELAY_KEY_WRITE - 345)) | (1 << (MySqlBaseParser.DES_KEY_FILE - 345)) | (1 << (MySqlBaseParser.DIRECTORY - 345)) | (1 << (MySqlBaseParser.DISABLE - 345)) | (1 << (MySqlBaseParser.DISCARD - 345)))) != 0) or ((((_la - 409)) & ~0x3f) == 0 and ((1 << (_la - 409)) & ((1 << (MySqlBaseParser.DISK - 409)) | (1 << (MySqlBaseParser.DO - 409)) | (1 << (MySqlBaseParser.DUMPFILE - 409)) | (1 << (MySqlBaseParser.DUPLICATE - 409)) | (1 << (MySqlBaseParser.DYNAMIC - 409)) | (1 << (MySqlBaseParser.ENABLE - 409)) | (1 << (MySqlBaseParser.ENCRYPTION - 409)) | (1 << (MySqlBaseParser.END - 409)) | (1 << (MySqlBaseParser.ENDS - 409)) | (1 << (MySqlBaseParser.ENGINE - 409)) | (1 << (MySqlBaseParser.ENGINES - 409)) | (1 << (MySqlBaseParser.ERROR - 409)) | (1 << (MySqlBaseParser.ERRORS - 409)) | (1 << (MySqlBaseParser.ESCAPE - 409)) | (1 << (MySqlBaseParser.EVEN - 409)) | (1 << (MySqlBaseParser.EVENT - 409)) | (1 << (MySqlBaseParser.EVENTS - 409)) | (1 << (MySqlBaseParser.EVERY - 409)) | (1 << (MySqlBaseParser.EXCHANGE - 409)) | (1 << (MySqlBaseParser.EXCLUSIVE - 409)) | (1 << (MySqlBaseParser.EXPIRE - 409)) | (1 << (MySqlBaseParser.EXPORT - 409)) | (1 << (MySqlBaseParser.EXTENDED - 409)) | (1 << (MySqlBaseParser.EXTENT_SIZE - 409)) | (1 << (MySqlBaseParser.FAST - 409)) | (1 << (MySqlBaseParser.FAULTS - 409)) | (1 << (MySqlBaseParser.FIELDS - 409)) | (1 << (MySqlBaseParser.FILE_BLOCK_SIZE - 409)) | (1 << (MySqlBaseParser.FILTER - 409)) | (1 << (MySqlBaseParser.FIRST - 409)) | (1 << (MySqlBaseParser.FIXED - 409)) | (1 << (MySqlBaseParser.FLUSH - 409)) | (1 << (MySqlBaseParser.FOLLOWS - 409)) | (1 << (MySqlBaseParser.FOUND - 409)) | (1 << (MySqlBaseParser.FULL - 409)) | (1 << (MySqlBaseParser.FUNCTION - 409)) | (1 << (MySqlBaseParser.GENERAL - 409)) | (1 << (MySqlBaseParser.GLOBAL - 409)) | (1 << (MySqlBaseParser.GRANTS - 409)) | (1 << (MySqlBaseParser.GROUP_REPLICATION - 409)) | (1 << (MySqlBaseParser.HANDLER - 409)) | (1 << (MySqlBaseParser.HASH - 409)) | (1 << (MySqlBaseParser.HELP - 409)) | (1 << (MySqlBaseParser.HOST - 409)) | (1 << (MySqlBaseParser.HOSTS - 409)) | (1 << (MySqlBaseParser.IDENTIFIED - 409)) | (1 << (MySqlBaseParser.IGNORE_SERVER_IDS - 409)) | (1 << (MySqlBaseParser.IMPORT - 409)) | (1 << (MySqlBaseParser.INDEXES - 409)) | (1 << (MySqlBaseParser.INITIAL_SIZE - 409)) | (1 << (MySqlBaseParser.INPLACE - 409)) | (1 << (MySqlBaseParser.INSERT_METHOD - 409)) | (1 << (MySqlBaseParser.INSTALL - 409)) | (1 << (MySqlBaseParser.INSTANCE - 409)) | (1 << (MySqlBaseParser.INVOKER - 409)) | (1 << (MySqlBaseParser.IO - 409)) | (1 << (MySqlBaseParser.IO_THREAD - 409)) | (1 << (MySqlBaseParser.IPC - 409)) | (1 << (MySqlBaseParser.ISOLATION - 409)) | (1 << (MySqlBaseParser.ISSUER - 409)) | (1 << (MySqlBaseParser.JSON - 409)) | (1 << (MySqlBaseParser.KEY_BLOCK_SIZE - 409)) | (1 << (MySqlBaseParser.LANGUAGE - 409)))) != 0) or ((((_la - 473)) & ~0x3f) == 0 and ((1 << (_la - 473)) & ((1 << (MySqlBaseParser.LAST - 473)) | (1 << (MySqlBaseParser.LEAVES - 473)) | (1 << (MySqlBaseParser.LESS - 473)) | (1 << (MySqlBaseParser.LEVEL - 473)) | (1 << (MySqlBaseParser.LIST - 473)) | (1 << (MySqlBaseParser.LOCAL - 473)) | (1 << (MySqlBaseParser.LOGFILE - 473)) | (1 << (MySqlBaseParser.LOGS - 473)) | (1 << (MySqlBaseParser.MASTER - 473)) | (1 << (MySqlBaseParser.MASTER_AUTO_POSITION - 473)) | (1 << (MySqlBaseParser.MASTER_CONNECT_RETRY - 473)) | (1 << (MySqlBaseParser.MASTER_DELAY - 473)) | (1 << (MySqlBaseParser.MASTER_HEARTBEAT_PERIOD - 473)) | (1 << (MySqlBaseParser.MASTER_HOST - 473)) | (1 << (MySqlBaseParser.MASTER_LOG_FILE - 473)) | (1 << (MySqlBaseParser.MASTER_LOG_POS - 473)) | (1 << (MySqlBaseParser.MASTER_PASSWORD - 473)) | (1 << (MySqlBaseParser.MASTER_PORT - 473)) | (1 << (MySqlBaseParser.MASTER_RETRY_COUNT - 473)) | (1 << (MySqlBaseParser.MASTER_SSL - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CA - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CAPATH - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CERT - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CIPHER - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CRL - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CRLPATH - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_KEY - 473)) | (1 << (MySqlBaseParser.MASTER_TLS_VERSION - 473)) | (1 << (MySqlBaseParser.MASTER_USER - 473)) | (1 << (MySqlBaseParser.MAX_CONNECTIONS_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_QUERIES_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_ROWS - 473)) | (1 << (MySqlBaseParser.MAX_SIZE - 473)) | (1 << (MySqlBaseParser.MAX_UPDATES_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_USER_CONNECTIONS - 473)) | (1 << (MySqlBaseParser.MEDIUM - 473)) | (1 << (MySqlBaseParser.MEMBER - 473)) | (1 << (MySqlBaseParser.MERGE - 473)) | (1 << (MySqlBaseParser.MESSAGE_TEXT - 473)) | (1 << (MySqlBaseParser.MID - 473)) | (1 << (MySqlBaseParser.MIGRATE - 473)) | (1 << (MySqlBaseParser.MIN_ROWS - 473)) | (1 << (MySqlBaseParser.MODE - 473)) | (1 << (MySqlBaseParser.MODIFY - 473)) | (1 << (MySqlBaseParser.MUTEX - 473)) | (1 << (MySqlBaseParser.MYSQL - 473)) | (1 << (MySqlBaseParser.MYSQL_ERRNO - 473)) | (1 << (MySqlBaseParser.NAME - 473)) | (1 << (MySqlBaseParser.NAMES - 473)) | (1 << (MySqlBaseParser.NCHAR - 473)) | (1 << (MySqlBaseParser.NEVER - 473)) | (1 << (MySqlBaseParser.NEXT - 473)) | (1 << (MySqlBaseParser.NO - 473)) | (1 << (MySqlBaseParser.NODEGROUP - 473)) | (1 << (MySqlBaseParser.NONE - 473)) | (1 << (MySqlBaseParser.ODBC - 473)) | (1 << (MySqlBaseParser.OFFLINE - 473)) | (1 << (MySqlBaseParser.OFFSET - 473)) | (1 << (MySqlBaseParser.OF - 473)) | (1 << (MySqlBaseParser.OJ - 473)) | (1 << (MySqlBaseParser.OLD_PASSWORD - 473)) | (1 << (MySqlBaseParser.ONE - 473)) | (1 << (MySqlBaseParser.ONLINE - 473)) | (1 << (MySqlBaseParser.ONLY - 473)))) != 0) or ((((_la - 537)) & ~0x3f) == 0 and ((1 << (_la - 537)) & ((1 << (MySqlBaseParser.OPEN - 537)) | (1 << (MySqlBaseParser.OPTIMIZER_COSTS - 537)) | (1 << (MySqlBaseParser.OPTIONS - 537)) | (1 << (MySqlBaseParser.OWNER - 537)) | (1 << (MySqlBaseParser.PACK_KEYS - 537)) | (1 << (MySqlBaseParser.PAGE - 537)) | (1 << (MySqlBaseParser.PARSER - 537)) | (1 << (MySqlBaseParser.PARTIAL - 537)) | (1 << (MySqlBaseParser.PARTITIONING - 537)) | (1 << (MySqlBaseParser.PARTITIONS - 537)) | (1 << (MySqlBaseParser.PASSWORD - 537)) | (1 << (MySqlBaseParser.PHASE - 537)) | (1 << (MySqlBaseParser.PLUGIN - 537)) | (1 << (MySqlBaseParser.PLUGIN_DIR - 537)) | (1 << (MySqlBaseParser.PLUGINS - 537)) | (1 << (MySqlBaseParser.PORT - 537)) | (1 << (MySqlBaseParser.PRECEDES - 537)) | (1 << (MySqlBaseParser.PREPARE - 537)) | (1 << (MySqlBaseParser.PRESERVE - 537)) | (1 << (MySqlBaseParser.PREV - 537)) | (1 << (MySqlBaseParser.PROCESSLIST - 537)) | (1 << (MySqlBaseParser.PROFILE - 537)) | (1 << (MySqlBaseParser.PROFILES - 537)) | (1 << (MySqlBaseParser.PROXY - 537)) | (1 << (MySqlBaseParser.QUERY - 537)) | (1 << (MySqlBaseParser.QUICK - 537)) | (1 << (MySqlBaseParser.REBUILD - 537)) | (1 << (MySqlBaseParser.RECOVER - 537)) | (1 << (MySqlBaseParser.REDO_BUFFER_SIZE - 537)) | (1 << (MySqlBaseParser.REDUNDANT - 537)) | (1 << (MySqlBaseParser.RELAY - 537)) | (1 << (MySqlBaseParser.RELAY_LOG_FILE - 537)) | (1 << (MySqlBaseParser.RELAY_LOG_POS - 537)) | (1 << (MySqlBaseParser.RELAYLOG - 537)) | (1 << (MySqlBaseParser.REMOVE - 537)) | (1 << (MySqlBaseParser.REORGANIZE - 537)) | (1 << (MySqlBaseParser.REPAIR - 537)) | (1 << (MySqlBaseParser.REPLICATE_DO_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_DO_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_IGNORE_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_IGNORE_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_REWRITE_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_WILD_DO_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_WILD_IGNORE_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATION - 537)) | (1 << (MySqlBaseParser.RESET - 537)) | (1 << (MySqlBaseParser.RESUME - 537)) | (1 << (MySqlBaseParser.RETURNED_SQLSTATE - 537)) | (1 << (MySqlBaseParser.RETURNS - 537)) | (1 << (MySqlBaseParser.ROLE - 537)) | (1 << (MySqlBaseParser.ROLLBACK - 537)) | (1 << (MySqlBaseParser.ROLLUP - 537)) | (1 << (MySqlBaseParser.ROTATE - 537)) | (1 << (MySqlBaseParser.ROW - 537)) | (1 << (MySqlBaseParser.ROWS - 537)) | (1 << (MySqlBaseParser.ROW_FORMAT - 537)) | (1 << (MySqlBaseParser.SAVEPOINT - 537)) | (1 << (MySqlBaseParser.SCHEDULE - 537)) | (1 << (MySqlBaseParser.SECURITY - 537)) | (1 << (MySqlBaseParser.SERVER - 537)) | (1 << (MySqlBaseParser.SESSION - 537)) | (1 << (MySqlBaseParser.SHARE - 537)) | (1 << (MySqlBaseParser.SHARED - 537)))) != 0) or ((((_la - 601)) & ~0x3f) == 0 and ((1 << (_la - 601)) & ((1 << (MySqlBaseParser.SIGNED - 601)) | (1 << (MySqlBaseParser.SIMPLE - 601)) | (1 << (MySqlBaseParser.SLAVE - 601)) | (1 << (MySqlBaseParser.SLOW - 601)) | (1 << (MySqlBaseParser.SNAPSHOT - 601)) | (1 << (MySqlBaseParser.SOCKET - 601)) | (1 << (MySqlBaseParser.SOME - 601)) | (1 << (MySqlBaseParser.SONAME - 601)) | (1 << (MySqlBaseParser.SOUNDS - 601)) | (1 << (MySqlBaseParser.SOURCE - 601)) | (1 << (MySqlBaseParser.SQL_AFTER_GTIDS - 601)) | (1 << (MySqlBaseParser.SQL_AFTER_MTS_GAPS - 601)) | (1 << (MySqlBaseParser.SQL_BEFORE_GTIDS - 601)) | (1 << (MySqlBaseParser.SQL_BUFFER_RESULT - 601)) | (1 << (MySqlBaseParser.SQL_CACHE - 601)) | (1 << (MySqlBaseParser.SQL_NO_CACHE - 601)) | (1 << (MySqlBaseParser.SQL_THREAD - 601)) | (1 << (MySqlBaseParser.START - 601)) | (1 << (MySqlBaseParser.STARTS - 601)) | (1 << (MySqlBaseParser.STATS_AUTO_RECALC - 601)) | (1 << (MySqlBaseParser.STATS_PERSISTENT - 601)) | (1 << (MySqlBaseParser.STATS_SAMPLE_PAGES - 601)) | (1 << (MySqlBaseParser.STATUS - 601)) | (1 << (MySqlBaseParser.STOP - 601)) | (1 << (MySqlBaseParser.STORAGE - 601)) | (1 << (MySqlBaseParser.STRING - 601)) | (1 << (MySqlBaseParser.SUBCLASS_ORIGIN - 601)) | (1 << (MySqlBaseParser.SUBJECT - 601)) | (1 << (MySqlBaseParser.SUBPARTITION - 601)) | (1 << (MySqlBaseParser.SUBPARTITIONS - 601)) | (1 << (MySqlBaseParser.SUSPEND - 601)) | (1 << (MySqlBaseParser.SWAPS - 601)) | (1 << (MySqlBaseParser.SWITCHES - 601)) | (1 << (MySqlBaseParser.TABLE_NAME - 601)) | (1 << (MySqlBaseParser.TABLESPACE - 601)) | (1 << (MySqlBaseParser.TEMPORARY - 601)) | (1 << (MySqlBaseParser.TEMPTABLE - 601)) | (1 << (MySqlBaseParser.THAN - 601)) | (1 << (MySqlBaseParser.TRADITIONAL - 601)) | (1 << (MySqlBaseParser.TRANSACTION - 601)) | (1 << (MySqlBaseParser.TRANSACTIONAL - 601)) | (1 << (MySqlBaseParser.TRIGGERS - 601)) | (1 << (MySqlBaseParser.TRUNCATE - 601)) | (1 << (MySqlBaseParser.UNDEFINED - 601)) | (1 << (MySqlBaseParser.UNDOFILE - 601)) | (1 << (MySqlBaseParser.UNDO_BUFFER_SIZE - 601)) | (1 << (MySqlBaseParser.UNINSTALL - 601)) | (1 << (MySqlBaseParser.UNKNOWN - 601)) | (1 << (MySqlBaseParser.UNTIL - 601)) | (1 << (MySqlBaseParser.UPGRADE - 601)) | (1 << (MySqlBaseParser.USER - 601)) | (1 << (MySqlBaseParser.USE_FRM - 601)) | (1 << (MySqlBaseParser.USER_RESOURCES - 601)) | (1 << (MySqlBaseParser.VALIDATION - 601)) | (1 << (MySqlBaseParser.VALUE - 601)) | (1 << (MySqlBaseParser.VARIABLES - 601)) | (1 << (MySqlBaseParser.VIEW - 601)) | (1 << (MySqlBaseParser.WAIT - 601)) | (1 << (MySqlBaseParser.WARNINGS - 601)) | (1 << (MySqlBaseParser.WITHOUT - 601)))) != 0) or ((((_la - 665)) & ~0x3f) == 0 and ((1 << (_la - 665)) & ((1 << (MySqlBaseParser.WORK - 665)) | (1 << (MySqlBaseParser.WRAPPER - 665)) | (1 << (MySqlBaseParser.X509 - 665)) | (1 << (MySqlBaseParser.XA - 665)) | (1 << (MySqlBaseParser.XML - 665)) | (1 << (MySqlBaseParser.INTERNAL - 665)) | (1 << (MySqlBaseParser.AUDIT_ADMIN - 665)) | (1 << (MySqlBaseParser.BACKUP_ADMIN - 665)) | (1 << (MySqlBaseParser.BINLOG_ADMIN - 665)) | (1 << (MySqlBaseParser.BINLOG_ENCRYPTION_ADMIN - 665)) | (1 << (MySqlBaseParser.CLONE_ADMIN - 665)) | (1 << (MySqlBaseParser.CONNECTION_ADMIN - 665)) | (1 << (MySqlBaseParser.ENCRYPTION_KEY_ADMIN - 665)) | (1 << (MySqlBaseParser.FIREWALL_ADMIN - 665)) | (1 << (MySqlBaseParser.FIREWALL_USER - 665)) | (1 << (MySqlBaseParser.GROUP_REPLICATION_ADMIN - 665)) | (1 << (MySqlBaseParser.INNODB_REDO_LOG_ARCHIVE - 665)) | (1 << (MySqlBaseParser.NDB_STORED_USER - 665)) | (1 << (MySqlBaseParser.PERSIST_RO_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.REPLICATION_APPLIER - 665)) | (1 << (MySqlBaseParser.REPLICATION_SLAVE_ADMIN - 665)) | (1 << (MySqlBaseParser.RESOURCE_GROUP_ADMIN - 665)) | (1 << (MySqlBaseParser.RESOURCE_GROUP_USER - 665)) | (1 << (MySqlBaseParser.ROLE_ADMIN - 665)) | (1 << (MySqlBaseParser.SESSION_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.SET_USER_ID - 665)) | (1 << (MySqlBaseParser.SHOW_ROUTINE - 665)) | (1 << (MySqlBaseParser.SYSTEM_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.TABLE_ENCRYPTION_ADMIN - 665)) | (1 << (MySqlBaseParser.VERSION_TOKEN_ADMIN - 665)) | (1 << (MySqlBaseParser.XA_RECOVER_ADMIN - 665)))) != 0) or _la==MySqlBaseParser.MEMORY or _la==MySqlBaseParser.CATALOG_NAME or _la==MySqlBaseParser.SCHEMA_NAME or ((((_la - 1082)) & ~0x3f) == 0 and ((1 << (_la - 1082)) & ((1 << (MySqlBaseParser.STRING_LITERAL - 1082)) | (1 << (MySqlBaseParser.ID - 1082)) | (1 << (MySqlBaseParser.OPTIONAL - 1082)))) != 0):
                    self.state = 239
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MySqlBaseParser.AS:
                        self.state = 238
                        self.match(MySqlBaseParser.AS)


                    self.state = 241
                    self.uid()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(MySqlBaseParser.TableNameContext,0)


        def tableAlias(self):
            return self.getTypedRuleContext(MySqlBaseParser.TableAliasContext,0)


        def AS(self):
            return self.getToken(MySqlBaseParser.AS, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_tableSource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSource" ):
                listener.enterTableSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSource" ):
                listener.exitTableSource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSource" ):
                return visitor.visitTableSource(self)
            else:
                return visitor.visitChildren(self)




    def tableSource(self):

        localctx = MySqlBaseParser.TableSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tableSource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.tableName()
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlBaseParser.AS:
                    self.state = 247
                    self.match(MySqlBaseParser.AS)


                self.state = 250
                self.tableAlias()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fullId(self):
            return self.getTypedRuleContext(MySqlBaseParser.FullIdContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = MySqlBaseParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.fullId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableAliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uid(self):
            return self.getTypedRuleContext(MySqlBaseParser.UidContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_tableAlias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableAlias" ):
                listener.enterTableAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableAlias" ):
                listener.exitTableAlias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableAlias" ):
                return visitor.visitTableAlias(self)
            else:
                return visitor.visitChildren(self)




    def tableAlias(self):

        localctx = MySqlBaseParser.TableAliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_tableAlias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.uid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FullIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.UidContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.UidContext,i)


        def DOT(self):
            return self.getToken(MySqlBaseParser.DOT, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_fullId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullId" ):
                listener.enterFullId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullId" ):
                listener.exitFullId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullId" ):
                return visitor.visitFullId(self)
            else:
                return visitor.visitChildren(self)




    def fullId(self):

        localctx = MySqlBaseParser.FullIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_fullId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.uid()
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(MySqlBaseParser.DOT)
                self.state = 259
                self.uid()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FullColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uid(self):
            return self.getTypedRuleContext(MySqlBaseParser.UidContext,0)


        def dottedId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.DottedIdContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.DottedIdContext,i)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_fullColumnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullColumnName" ):
                listener.enterFullColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullColumnName" ):
                listener.exitFullColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullColumnName" ):
                return visitor.visitFullColumnName(self)
            else:
                return visitor.visitChildren(self)




    def fullColumnName(self):

        localctx = MySqlBaseParser.FullColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fullColumnName)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.uid()
                self.state = 267
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 263
                    self.dottedId()
                    self.state = 265
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 264
                        self.dottedId()




                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.matchWildcard()
                self.state = 270
                self.dottedId()
                self.state = 272
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 271
                    self.dottedId()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DottedIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT_ID(self):
            return self.getToken(MySqlBaseParser.DOT_ID, 0)

        def DOT(self):
            return self.getToken(MySqlBaseParser.DOT, 0)

        def uid(self):
            return self.getTypedRuleContext(MySqlBaseParser.UidContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_dottedId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDottedId" ):
                listener.enterDottedId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDottedId" ):
                listener.exitDottedId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDottedId" ):
                return visitor.visitDottedId(self)
            else:
                return visitor.visitChildren(self)




    def dottedId(self):

        localctx = MySqlBaseParser.DottedIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dottedId)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.DOT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(MySqlBaseParser.DOT_ID)
                pass
            elif token in [MySqlBaseParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(MySqlBaseParser.DOT)
                self.state = 278
                self.uid()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UidListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.UidContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.UidContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.COMMA)
            else:
                return self.getToken(MySqlBaseParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_uidList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUidList" ):
                listener.enterUidList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUidList" ):
                listener.exitUidList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUidList" ):
                return visitor.visitUidList(self)
            else:
                return visitor.visitChildren(self)




    def uidList(self):

        localctx = MySqlBaseParser.UidListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_uidList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.uid()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlBaseParser.COMMA:
                self.state = 282
                self.match(MySqlBaseParser.COMMA)
                self.state = 283
                self.uid()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySqlBaseParser.ID, 0)

        def keywordsCanBeId(self):
            return self.getTypedRuleContext(MySqlBaseParser.KeywordsCanBeIdContext,0)


        def stringLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.StringLiteralContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_uid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUid" ):
                listener.enterUid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUid" ):
                listener.exitUid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUid" ):
                return visitor.visitUid(self)
            else:
                return visitor.visitChildren(self)




    def uid(self):

        localctx = MySqlBaseParser.UidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_uid)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(MySqlBaseParser.ID)
                pass
            elif token in [MySqlBaseParser.CURRENT, MySqlBaseParser.DIAGNOSTICS, MySqlBaseParser.GROUP, MySqlBaseParser.NUMBER, MySqlBaseParser.ORDER, MySqlBaseParser.STACKED, MySqlBaseParser.SERIAL, MySqlBaseParser.AVG, MySqlBaseParser.BIT_AND, MySqlBaseParser.BIT_OR, MySqlBaseParser.BIT_XOR, MySqlBaseParser.COUNT, MySqlBaseParser.GROUP_CONCAT, MySqlBaseParser.MAX, MySqlBaseParser.MIN, MySqlBaseParser.STD, MySqlBaseParser.STDDEV, MySqlBaseParser.STDDEV_POP, MySqlBaseParser.STDDEV_SAMP, MySqlBaseParser.SUM, MySqlBaseParser.VAR_POP, MySqlBaseParser.VAR_SAMP, MySqlBaseParser.VARIANCE, MySqlBaseParser.ACCOUNT, MySqlBaseParser.ACTION, MySqlBaseParser.AFTER, MySqlBaseParser.AGGREGATE, MySqlBaseParser.ALGORITHM, MySqlBaseParser.ANY, MySqlBaseParser.AT, MySqlBaseParser.AUTHORS, MySqlBaseParser.AUTOCOMMIT, MySqlBaseParser.AUTOEXTEND_SIZE, MySqlBaseParser.AUTO_INCREMENT, MySqlBaseParser.AVG_ROW_LENGTH, MySqlBaseParser.BEGIN, MySqlBaseParser.BINLOG, MySqlBaseParser.BIT, MySqlBaseParser.BLOCK, MySqlBaseParser.BOOL, MySqlBaseParser.BOOLEAN, MySqlBaseParser.BTREE, MySqlBaseParser.CACHE, MySqlBaseParser.CASCADED, MySqlBaseParser.CHAIN, MySqlBaseParser.CHANGED, MySqlBaseParser.CHANNEL, MySqlBaseParser.CHECKSUM, MySqlBaseParser.PAGE_CHECKSUM, MySqlBaseParser.CIPHER, MySqlBaseParser.CLASS_ORIGIN, MySqlBaseParser.CLIENT, MySqlBaseParser.CLOSE, MySqlBaseParser.COALESCE, MySqlBaseParser.CODE, MySqlBaseParser.COLUMNS, MySqlBaseParser.COLUMN_FORMAT, MySqlBaseParser.COLUMN_NAME, MySqlBaseParser.COMMENT, MySqlBaseParser.COMMIT, MySqlBaseParser.COMPACT, MySqlBaseParser.COMPLETION, MySqlBaseParser.COMPRESSED, MySqlBaseParser.COMPRESSION, MySqlBaseParser.CONCURRENT, MySqlBaseParser.CONNECT, MySqlBaseParser.CONNECTION, MySqlBaseParser.CONSISTENT, MySqlBaseParser.CONSTRAINT_CATALOG, MySqlBaseParser.CONSTRAINT_SCHEMA, MySqlBaseParser.CONSTRAINT_NAME, MySqlBaseParser.CONTAINS, MySqlBaseParser.CONTEXT, MySqlBaseParser.CONTRIBUTORS, MySqlBaseParser.COPY, MySqlBaseParser.CPU, MySqlBaseParser.CURSOR_NAME, MySqlBaseParser.DATA, MySqlBaseParser.DATAFILE, MySqlBaseParser.DEALLOCATE, MySqlBaseParser.DEFAULT_AUTH, MySqlBaseParser.DEFINER, MySqlBaseParser.DELAY_KEY_WRITE, MySqlBaseParser.DES_KEY_FILE, MySqlBaseParser.DIRECTORY, MySqlBaseParser.DISABLE, MySqlBaseParser.DISCARD, MySqlBaseParser.DISK, MySqlBaseParser.DO, MySqlBaseParser.DUMPFILE, MySqlBaseParser.DUPLICATE, MySqlBaseParser.DYNAMIC, MySqlBaseParser.ENABLE, MySqlBaseParser.ENCRYPTION, MySqlBaseParser.END, MySqlBaseParser.ENDS, MySqlBaseParser.ENGINE, MySqlBaseParser.ENGINES, MySqlBaseParser.ERROR, MySqlBaseParser.ERRORS, MySqlBaseParser.ESCAPE, MySqlBaseParser.EVEN, MySqlBaseParser.EVENT, MySqlBaseParser.EVENTS, MySqlBaseParser.EVERY, MySqlBaseParser.EXCHANGE, MySqlBaseParser.EXCLUSIVE, MySqlBaseParser.EXPIRE, MySqlBaseParser.EXPORT, MySqlBaseParser.EXTENDED, MySqlBaseParser.EXTENT_SIZE, MySqlBaseParser.FAST, MySqlBaseParser.FAULTS, MySqlBaseParser.FIELDS, MySqlBaseParser.FILE_BLOCK_SIZE, MySqlBaseParser.FILTER, MySqlBaseParser.FIRST, MySqlBaseParser.FIXED, MySqlBaseParser.FLUSH, MySqlBaseParser.FOLLOWS, MySqlBaseParser.FOUND, MySqlBaseParser.FULL, MySqlBaseParser.FUNCTION, MySqlBaseParser.GENERAL, MySqlBaseParser.GLOBAL, MySqlBaseParser.GRANTS, MySqlBaseParser.GROUP_REPLICATION, MySqlBaseParser.HANDLER, MySqlBaseParser.HASH, MySqlBaseParser.HELP, MySqlBaseParser.HOST, MySqlBaseParser.HOSTS, MySqlBaseParser.IDENTIFIED, MySqlBaseParser.IGNORE_SERVER_IDS, MySqlBaseParser.IMPORT, MySqlBaseParser.INDEXES, MySqlBaseParser.INITIAL_SIZE, MySqlBaseParser.INPLACE, MySqlBaseParser.INSERT_METHOD, MySqlBaseParser.INSTALL, MySqlBaseParser.INSTANCE, MySqlBaseParser.INVOKER, MySqlBaseParser.IO, MySqlBaseParser.IO_THREAD, MySqlBaseParser.IPC, MySqlBaseParser.ISOLATION, MySqlBaseParser.ISSUER, MySqlBaseParser.JSON, MySqlBaseParser.KEY_BLOCK_SIZE, MySqlBaseParser.LANGUAGE, MySqlBaseParser.LAST, MySqlBaseParser.LEAVES, MySqlBaseParser.LESS, MySqlBaseParser.LEVEL, MySqlBaseParser.LIST, MySqlBaseParser.LOCAL, MySqlBaseParser.LOGFILE, MySqlBaseParser.LOGS, MySqlBaseParser.MASTER, MySqlBaseParser.MASTER_AUTO_POSITION, MySqlBaseParser.MASTER_CONNECT_RETRY, MySqlBaseParser.MASTER_DELAY, MySqlBaseParser.MASTER_HEARTBEAT_PERIOD, MySqlBaseParser.MASTER_HOST, MySqlBaseParser.MASTER_LOG_FILE, MySqlBaseParser.MASTER_LOG_POS, MySqlBaseParser.MASTER_PASSWORD, MySqlBaseParser.MASTER_PORT, MySqlBaseParser.MASTER_RETRY_COUNT, MySqlBaseParser.MASTER_SSL, MySqlBaseParser.MASTER_SSL_CA, MySqlBaseParser.MASTER_SSL_CAPATH, MySqlBaseParser.MASTER_SSL_CERT, MySqlBaseParser.MASTER_SSL_CIPHER, MySqlBaseParser.MASTER_SSL_CRL, MySqlBaseParser.MASTER_SSL_CRLPATH, MySqlBaseParser.MASTER_SSL_KEY, MySqlBaseParser.MASTER_TLS_VERSION, MySqlBaseParser.MASTER_USER, MySqlBaseParser.MAX_CONNECTIONS_PER_HOUR, MySqlBaseParser.MAX_QUERIES_PER_HOUR, MySqlBaseParser.MAX_ROWS, MySqlBaseParser.MAX_SIZE, MySqlBaseParser.MAX_UPDATES_PER_HOUR, MySqlBaseParser.MAX_USER_CONNECTIONS, MySqlBaseParser.MEDIUM, MySqlBaseParser.MEMBER, MySqlBaseParser.MERGE, MySqlBaseParser.MESSAGE_TEXT, MySqlBaseParser.MID, MySqlBaseParser.MIGRATE, MySqlBaseParser.MIN_ROWS, MySqlBaseParser.MODE, MySqlBaseParser.MODIFY, MySqlBaseParser.MUTEX, MySqlBaseParser.MYSQL, MySqlBaseParser.MYSQL_ERRNO, MySqlBaseParser.NAME, MySqlBaseParser.NAMES, MySqlBaseParser.NCHAR, MySqlBaseParser.NEVER, MySqlBaseParser.NEXT, MySqlBaseParser.NO, MySqlBaseParser.NODEGROUP, MySqlBaseParser.NONE, MySqlBaseParser.ODBC, MySqlBaseParser.OFFLINE, MySqlBaseParser.OFFSET, MySqlBaseParser.OF, MySqlBaseParser.OJ, MySqlBaseParser.OLD_PASSWORD, MySqlBaseParser.ONE, MySqlBaseParser.ONLINE, MySqlBaseParser.ONLY, MySqlBaseParser.OPEN, MySqlBaseParser.OPTIMIZER_COSTS, MySqlBaseParser.OPTIONS, MySqlBaseParser.OWNER, MySqlBaseParser.PACK_KEYS, MySqlBaseParser.PAGE, MySqlBaseParser.PARSER, MySqlBaseParser.PARTIAL, MySqlBaseParser.PARTITIONING, MySqlBaseParser.PARTITIONS, MySqlBaseParser.PASSWORD, MySqlBaseParser.PHASE, MySqlBaseParser.PLUGIN, MySqlBaseParser.PLUGIN_DIR, MySqlBaseParser.PLUGINS, MySqlBaseParser.PORT, MySqlBaseParser.PRECEDES, MySqlBaseParser.PREPARE, MySqlBaseParser.PRESERVE, MySqlBaseParser.PREV, MySqlBaseParser.PROCESSLIST, MySqlBaseParser.PROFILE, MySqlBaseParser.PROFILES, MySqlBaseParser.PROXY, MySqlBaseParser.QUERY, MySqlBaseParser.QUICK, MySqlBaseParser.REBUILD, MySqlBaseParser.RECOVER, MySqlBaseParser.REDO_BUFFER_SIZE, MySqlBaseParser.REDUNDANT, MySqlBaseParser.RELAY, MySqlBaseParser.RELAY_LOG_FILE, MySqlBaseParser.RELAY_LOG_POS, MySqlBaseParser.RELAYLOG, MySqlBaseParser.REMOVE, MySqlBaseParser.REORGANIZE, MySqlBaseParser.REPAIR, MySqlBaseParser.REPLICATE_DO_DB, MySqlBaseParser.REPLICATE_DO_TABLE, MySqlBaseParser.REPLICATE_IGNORE_DB, MySqlBaseParser.REPLICATE_IGNORE_TABLE, MySqlBaseParser.REPLICATE_REWRITE_DB, MySqlBaseParser.REPLICATE_WILD_DO_TABLE, MySqlBaseParser.REPLICATE_WILD_IGNORE_TABLE, MySqlBaseParser.REPLICATION, MySqlBaseParser.RESET, MySqlBaseParser.RESUME, MySqlBaseParser.RETURNED_SQLSTATE, MySqlBaseParser.RETURNS, MySqlBaseParser.ROLE, MySqlBaseParser.ROLLBACK, MySqlBaseParser.ROLLUP, MySqlBaseParser.ROTATE, MySqlBaseParser.ROW, MySqlBaseParser.ROWS, MySqlBaseParser.ROW_FORMAT, MySqlBaseParser.SAVEPOINT, MySqlBaseParser.SCHEDULE, MySqlBaseParser.SECURITY, MySqlBaseParser.SERVER, MySqlBaseParser.SESSION, MySqlBaseParser.SHARE, MySqlBaseParser.SHARED, MySqlBaseParser.SIGNED, MySqlBaseParser.SIMPLE, MySqlBaseParser.SLAVE, MySqlBaseParser.SLOW, MySqlBaseParser.SNAPSHOT, MySqlBaseParser.SOCKET, MySqlBaseParser.SOME, MySqlBaseParser.SONAME, MySqlBaseParser.SOUNDS, MySqlBaseParser.SOURCE, MySqlBaseParser.SQL_AFTER_GTIDS, MySqlBaseParser.SQL_AFTER_MTS_GAPS, MySqlBaseParser.SQL_BEFORE_GTIDS, MySqlBaseParser.SQL_BUFFER_RESULT, MySqlBaseParser.SQL_CACHE, MySqlBaseParser.SQL_NO_CACHE, MySqlBaseParser.SQL_THREAD, MySqlBaseParser.START, MySqlBaseParser.STARTS, MySqlBaseParser.STATS_AUTO_RECALC, MySqlBaseParser.STATS_PERSISTENT, MySqlBaseParser.STATS_SAMPLE_PAGES, MySqlBaseParser.STATUS, MySqlBaseParser.STOP, MySqlBaseParser.STORAGE, MySqlBaseParser.STRING, MySqlBaseParser.SUBCLASS_ORIGIN, MySqlBaseParser.SUBJECT, MySqlBaseParser.SUBPARTITION, MySqlBaseParser.SUBPARTITIONS, MySqlBaseParser.SUSPEND, MySqlBaseParser.SWAPS, MySqlBaseParser.SWITCHES, MySqlBaseParser.TABLE_NAME, MySqlBaseParser.TABLESPACE, MySqlBaseParser.TEMPORARY, MySqlBaseParser.TEMPTABLE, MySqlBaseParser.THAN, MySqlBaseParser.TRADITIONAL, MySqlBaseParser.TRANSACTION, MySqlBaseParser.TRANSACTIONAL, MySqlBaseParser.TRIGGERS, MySqlBaseParser.TRUNCATE, MySqlBaseParser.UNDEFINED, MySqlBaseParser.UNDOFILE, MySqlBaseParser.UNDO_BUFFER_SIZE, MySqlBaseParser.UNINSTALL, MySqlBaseParser.UNKNOWN, MySqlBaseParser.UNTIL, MySqlBaseParser.UPGRADE, MySqlBaseParser.USER, MySqlBaseParser.USE_FRM, MySqlBaseParser.USER_RESOURCES, MySqlBaseParser.VALIDATION, MySqlBaseParser.VALUE, MySqlBaseParser.VARIABLES, MySqlBaseParser.VIEW, MySqlBaseParser.WAIT, MySqlBaseParser.WARNINGS, MySqlBaseParser.WITHOUT, MySqlBaseParser.WORK, MySqlBaseParser.WRAPPER, MySqlBaseParser.X509, MySqlBaseParser.XA, MySqlBaseParser.XML, MySqlBaseParser.INTERNAL, MySqlBaseParser.AUDIT_ADMIN, MySqlBaseParser.BACKUP_ADMIN, MySqlBaseParser.BINLOG_ADMIN, MySqlBaseParser.BINLOG_ENCRYPTION_ADMIN, MySqlBaseParser.CLONE_ADMIN, MySqlBaseParser.CONNECTION_ADMIN, MySqlBaseParser.ENCRYPTION_KEY_ADMIN, MySqlBaseParser.FIREWALL_ADMIN, MySqlBaseParser.FIREWALL_USER, MySqlBaseParser.GROUP_REPLICATION_ADMIN, MySqlBaseParser.INNODB_REDO_LOG_ARCHIVE, MySqlBaseParser.NDB_STORED_USER, MySqlBaseParser.PERSIST_RO_VARIABLES_ADMIN, MySqlBaseParser.REPLICATION_APPLIER, MySqlBaseParser.REPLICATION_SLAVE_ADMIN, MySqlBaseParser.RESOURCE_GROUP_ADMIN, MySqlBaseParser.RESOURCE_GROUP_USER, MySqlBaseParser.ROLE_ADMIN, MySqlBaseParser.SESSION_VARIABLES_ADMIN, MySqlBaseParser.SET_USER_ID, MySqlBaseParser.SHOW_ROUTINE, MySqlBaseParser.SYSTEM_VARIABLES_ADMIN, MySqlBaseParser.TABLE_ENCRYPTION_ADMIN, MySqlBaseParser.VERSION_TOKEN_ADMIN, MySqlBaseParser.XA_RECOVER_ADMIN, MySqlBaseParser.MEMORY, MySqlBaseParser.CATALOG_NAME, MySqlBaseParser.SCHEMA_NAME, MySqlBaseParser.OPTIONAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.keywordsCanBeId()
                pass
            elif token in [MySqlBaseParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.stringLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdatedElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fullColumnName(self):
            return self.getTypedRuleContext(MySqlBaseParser.FullColumnNameContext,0)


        def EQUAL_SYMBOL(self):
            return self.getToken(MySqlBaseParser.EQUAL_SYMBOL, 0)

        def expression(self):
            return self.getTypedRuleContext(MySqlBaseParser.ExpressionContext,0)


        def DEFAULT(self):
            return self.getToken(MySqlBaseParser.DEFAULT, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_updatedElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdatedElement" ):
                listener.enterUpdatedElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdatedElement" ):
                listener.exitUpdatedElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdatedElement" ):
                return visitor.visitUpdatedElement(self)
            else:
                return visitor.visitChildren(self)




    def updatedElement(self):

        localctx = MySqlBaseParser.UpdatedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_updatedElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.fullColumnName()
            self.state = 295
            self.match(MySqlBaseParser.EQUAL_SYMBOL)
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 296
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 297
                self.match(MySqlBaseParser.DEFAULT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(MySqlBaseParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(MySqlBaseParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = MySqlBaseParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MySqlBaseParser.WHERE)
            self.state = 301
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.COMMA)
            else:
                return self.getToken(MySqlBaseParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressions" ):
                listener.enterExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressions" ):
                listener.exitExpressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = MySqlBaseParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.expression(0)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlBaseParser.COMMA:
                self.state = 304
                self.match(MySqlBaseParser.COMMA)
                self.state = 305
                self.expression(0)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComparisonPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.PredicateContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.PredicateContext,i)

        def comparisonOperator(self):
            return self.getTypedRuleContext(MySqlBaseParser.ComparisonOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonPredicate" ):
                listener.enterComparisonPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonPredicate" ):
                listener.exitComparisonPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonPredicate" ):
                return visitor.visitComparisonPredicate(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionAtomPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlBaseParser.PredicateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionAtomPredicate" ):
                listener.enterExpressionAtomPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionAtomPredicate" ):
                listener.exitExpressionAtomPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAtomPredicate" ):
                return visitor.visitExpressionAtomPredicate(self)
            else:
                return visitor.visitChildren(self)


    class InPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlBaseParser.PredicateContext,0)

        def IN(self):
            return self.getToken(MySqlBaseParser.IN, 0)
        def LR_BRACKET(self):
            return self.getToken(MySqlBaseParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(MySqlBaseParser.RR_BRACKET, 0)
        def expressions(self):
            return self.getTypedRuleContext(MySqlBaseParser.ExpressionsContext,0)

        def NOT(self):
            return self.getToken(MySqlBaseParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInPredicate" ):
                listener.enterInPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInPredicate" ):
                listener.exitInPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInPredicate" ):
                return visitor.visitInPredicate(self)
            else:
                return visitor.visitChildren(self)


    class BetweenPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.PredicateContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.PredicateContext,i)

        def BETWEEN(self):
            return self.getToken(MySqlBaseParser.BETWEEN, 0)
        def AND(self):
            return self.getToken(MySqlBaseParser.AND, 0)
        def NOT(self):
            return self.getToken(MySqlBaseParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenPredicate" ):
                listener.enterBetweenPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenPredicate" ):
                listener.exitBetweenPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenPredicate" ):
                return visitor.visitBetweenPredicate(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MySqlBaseParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MySqlBaseParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class LikePredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.PredicateContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.PredicateContext,i)

        def LIKE(self):
            return self.getToken(MySqlBaseParser.LIKE, 0)
        def NOT(self):
            return self.getToken(MySqlBaseParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLikePredicate" ):
                listener.enterLikePredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLikePredicate" ):
                listener.exitLikePredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLikePredicate" ):
                return visitor.visitLikePredicate(self)
            else:
                return visitor.visitChildren(self)


    class NullPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlBaseParser.PredicateContext,0)

        def IS(self):
            return self.getToken(MySqlBaseParser.IS, 0)
        def nullLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.NullLiteralContext,0)

        def NOT(self):
            return self.getToken(MySqlBaseParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullPredicate" ):
                listener.enterNullPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullPredicate" ):
                listener.exitNullPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullPredicate" ):
                return visitor.visitNullPredicate(self)
            else:
                return visitor.visitChildren(self)


    class LogicalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.ExpressionContext,i)

        def logicalOperator(self):
            return self.getTypedRuleContext(MySqlBaseParser.LogicalOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MySqlBaseParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = MySqlBaseParser.InPredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 312
                self.predicate()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlBaseParser.NOT:
                    self.state = 313
                    self.match(MySqlBaseParser.NOT)


                self.state = 316
                self.match(MySqlBaseParser.IN)
                self.state = 317
                self.match(MySqlBaseParser.LR_BRACKET)

                self.state = 318
                self.expressions()
                self.state = 319
                self.match(MySqlBaseParser.RR_BRACKET)
                pass

            elif la_ == 2:
                localctx = MySqlBaseParser.ComparisonPredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 321
                self.predicate()
                self.state = 322
                self.comparisonOperator()
                self.state = 323
                self.predicate()
                pass

            elif la_ == 3:
                localctx = MySqlBaseParser.NullPredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 325
                self.predicate()
                self.state = 326
                self.match(MySqlBaseParser.IS)
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlBaseParser.NOT:
                    self.state = 327
                    self.match(MySqlBaseParser.NOT)


                self.state = 330
                self.nullLiteral()
                pass

            elif la_ == 4:
                localctx = MySqlBaseParser.BetweenPredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 332
                self.predicate()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlBaseParser.NOT:
                    self.state = 333
                    self.match(MySqlBaseParser.NOT)


                self.state = 336
                self.match(MySqlBaseParser.BETWEEN)
                self.state = 337
                self.predicate()
                self.state = 338
                self.match(MySqlBaseParser.AND)
                self.state = 339
                self.predicate()
                pass

            elif la_ == 5:
                localctx = MySqlBaseParser.LikePredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 341
                self.predicate()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlBaseParser.NOT:
                    self.state = 342
                    self.match(MySqlBaseParser.NOT)


                self.state = 345
                self.match(MySqlBaseParser.LIKE)
                self.state = 346
                self.predicate()
                pass

            elif la_ == 6:
                localctx = MySqlBaseParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 348
                self.match(MySqlBaseParser.NOT)
                self.state = 349
                self.expression(3)
                pass

            elif la_ == 7:
                localctx = MySqlBaseParser.ExpressionAtomPredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 350
                self.predicate()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MySqlBaseParser.LogicalExpressionContext(self, MySqlBaseParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    self.logicalOperator()
                    self.state = 355
                    self.expression(3) 
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fullColumnName(self):
            return self.getTypedRuleContext(MySqlBaseParser.FullColumnNameContext,0)


        def constant(self):
            return self.getTypedRuleContext(MySqlBaseParser.ConstantContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MySqlBaseParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = MySqlBaseParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_predicate)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.fullColumnName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 364
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_functionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SpecificFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def specificFunction(self):
            return self.getTypedRuleContext(MySqlBaseParser.SpecificFunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecificFunctionCall" ):
                listener.enterSpecificFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecificFunctionCall" ):
                listener.exitSpecificFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecificFunctionCall" ):
                return visitor.visitSpecificFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class ScalarFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def scalarFunctionName(self):
            return self.getTypedRuleContext(MySqlBaseParser.ScalarFunctionNameContext,0)

        def LR_BRACKET(self):
            return self.getToken(MySqlBaseParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(MySqlBaseParser.RR_BRACKET, 0)
        def functionArgs(self):
            return self.getTypedRuleContext(MySqlBaseParser.FunctionArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalarFunctionCall" ):
                listener.enterScalarFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalarFunctionCall" ):
                listener.exitScalarFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarFunctionCall" ):
                return visitor.visitScalarFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def functionCall(self):

        localctx = MySqlBaseParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionCall)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                localctx = MySqlBaseParser.SpecificFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.specificFunction()
                pass

            elif la_ == 2:
                localctx = MySqlBaseParser.ScalarFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.scalarFunctionName()
                self.state = 369
                self.match(MySqlBaseParser.LR_BRACKET)
                self.state = 371
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 370
                    self.functionArgs()


                self.state = 373
                self.match(MySqlBaseParser.RR_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarFunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionNameBase(self):
            return self.getTypedRuleContext(MySqlBaseParser.FunctionNameBaseContext,0)


        def ASCII(self):
            return self.getToken(MySqlBaseParser.ASCII, 0)

        def CURDATE(self):
            return self.getToken(MySqlBaseParser.CURDATE, 0)

        def CURRENT_DATE(self):
            return self.getToken(MySqlBaseParser.CURRENT_DATE, 0)

        def CURRENT_TIME(self):
            return self.getToken(MySqlBaseParser.CURRENT_TIME, 0)

        def CURRENT_TIMESTAMP(self):
            return self.getToken(MySqlBaseParser.CURRENT_TIMESTAMP, 0)

        def CURTIME(self):
            return self.getToken(MySqlBaseParser.CURTIME, 0)

        def DATE_ADD(self):
            return self.getToken(MySqlBaseParser.DATE_ADD, 0)

        def DATE_SUB(self):
            return self.getToken(MySqlBaseParser.DATE_SUB, 0)

        def IF(self):
            return self.getToken(MySqlBaseParser.IF, 0)

        def INSERT(self):
            return self.getToken(MySqlBaseParser.INSERT, 0)

        def LOCALTIME(self):
            return self.getToken(MySqlBaseParser.LOCALTIME, 0)

        def LOCALTIMESTAMP(self):
            return self.getToken(MySqlBaseParser.LOCALTIMESTAMP, 0)

        def MID(self):
            return self.getToken(MySqlBaseParser.MID, 0)

        def NOW(self):
            return self.getToken(MySqlBaseParser.NOW, 0)

        def REPLACE(self):
            return self.getToken(MySqlBaseParser.REPLACE, 0)

        def SUBSTR(self):
            return self.getToken(MySqlBaseParser.SUBSTR, 0)

        def SUBSTRING(self):
            return self.getToken(MySqlBaseParser.SUBSTRING, 0)

        def SYSDATE(self):
            return self.getToken(MySqlBaseParser.SYSDATE, 0)

        def TRIM(self):
            return self.getToken(MySqlBaseParser.TRIM, 0)

        def UTC_DATE(self):
            return self.getToken(MySqlBaseParser.UTC_DATE, 0)

        def UTC_TIME(self):
            return self.getToken(MySqlBaseParser.UTC_TIME, 0)

        def UTC_TIMESTAMP(self):
            return self.getToken(MySqlBaseParser.UTC_TIMESTAMP, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_scalarFunctionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalarFunctionName" ):
                listener.enterScalarFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalarFunctionName" ):
                listener.exitScalarFunctionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarFunctionName" ):
                return visitor.visitScalarFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def scalarFunctionName(self):

        localctx = MySqlBaseParser.ScalarFunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_scalarFunctionName)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.MOD, MySqlBaseParser.DATABASE, MySqlBaseParser.LEFT, MySqlBaseParser.RIGHT, MySqlBaseParser.SCHEMA, MySqlBaseParser.DATE, MySqlBaseParser.TIME, MySqlBaseParser.TIMESTAMP, MySqlBaseParser.YEAR, MySqlBaseParser.JSON_ARRAY, MySqlBaseParser.JSON_OBJECT, MySqlBaseParser.JSON_QUOTE, MySqlBaseParser.JSON_CONTAINS, MySqlBaseParser.JSON_CONTAINS_PATH, MySqlBaseParser.JSON_EXTRACT, MySqlBaseParser.JSON_KEYS, MySqlBaseParser.JSON_OVERLAPS, MySqlBaseParser.JSON_SEARCH, MySqlBaseParser.JSON_VALUE, MySqlBaseParser.JSON_ARRAY_APPEND, MySqlBaseParser.JSON_ARRAY_INSERT, MySqlBaseParser.JSON_INSERT, MySqlBaseParser.JSON_MERGE, MySqlBaseParser.JSON_MERGE_PATCH, MySqlBaseParser.JSON_MERGE_PRESERVE, MySqlBaseParser.JSON_REMOVE, MySqlBaseParser.JSON_REPLACE, MySqlBaseParser.JSON_SET, MySqlBaseParser.JSON_UNQUOTE, MySqlBaseParser.JSON_DEPTH, MySqlBaseParser.JSON_LENGTH, MySqlBaseParser.JSON_TYPE, MySqlBaseParser.JSON_VALID, MySqlBaseParser.JSON_TABLE, MySqlBaseParser.JSON_SCHEMA_VALID, MySqlBaseParser.JSON_SCHEMA_VALIDATION_REPORT, MySqlBaseParser.JSON_PRETTY, MySqlBaseParser.JSON_STORAGE_FREE, MySqlBaseParser.JSON_STORAGE_SIZE, MySqlBaseParser.JSON_ARRAYAGG, MySqlBaseParser.JSON_OBJECTAGG, MySqlBaseParser.COUNT, MySqlBaseParser.POSITION, MySqlBaseParser.INVISIBLE, MySqlBaseParser.VISIBLE, MySqlBaseParser.QUARTER, MySqlBaseParser.MONTH, MySqlBaseParser.DAY, MySqlBaseParser.HOUR, MySqlBaseParser.MINUTE, MySqlBaseParser.WEEK, MySqlBaseParser.SECOND, MySqlBaseParser.MICROSECOND, MySqlBaseParser.SESSION_VARIABLES_ADMIN, MySqlBaseParser.GEOMETRYCOLLECTION, MySqlBaseParser.LINESTRING, MySqlBaseParser.MULTILINESTRING, MySqlBaseParser.MULTIPOINT, MySqlBaseParser.MULTIPOLYGON, MySqlBaseParser.POINT, MySqlBaseParser.POLYGON, MySqlBaseParser.ABS, MySqlBaseParser.ACOS, MySqlBaseParser.ADDDATE, MySqlBaseParser.ADDTIME, MySqlBaseParser.AES_DECRYPT, MySqlBaseParser.AES_ENCRYPT, MySqlBaseParser.AREA, MySqlBaseParser.ASBINARY, MySqlBaseParser.ASIN, MySqlBaseParser.ASTEXT, MySqlBaseParser.ASWKB, MySqlBaseParser.ASWKT, MySqlBaseParser.ASYMMETRIC_DECRYPT, MySqlBaseParser.ASYMMETRIC_DERIVE, MySqlBaseParser.ASYMMETRIC_ENCRYPT, MySqlBaseParser.ASYMMETRIC_SIGN, MySqlBaseParser.ASYMMETRIC_VERIFY, MySqlBaseParser.ATAN, MySqlBaseParser.ATAN2, MySqlBaseParser.BENCHMARK, MySqlBaseParser.BIN, MySqlBaseParser.BIT_COUNT, MySqlBaseParser.BIT_LENGTH, MySqlBaseParser.BUFFER, MySqlBaseParser.CEIL, MySqlBaseParser.CEILING, MySqlBaseParser.CENTROID, MySqlBaseParser.CHARACTER_LENGTH, MySqlBaseParser.CHARSET, MySqlBaseParser.CHAR_LENGTH, MySqlBaseParser.COERCIBILITY, MySqlBaseParser.COLLATION, MySqlBaseParser.COMPRESS, MySqlBaseParser.CONCAT, MySqlBaseParser.CONCAT_WS, MySqlBaseParser.CONNECTION_ID, MySqlBaseParser.CONV, MySqlBaseParser.CONVERT_TZ, MySqlBaseParser.COS, MySqlBaseParser.COT, MySqlBaseParser.CRC32, MySqlBaseParser.CREATE_ASYMMETRIC_PRIV_KEY, MySqlBaseParser.CREATE_ASYMMETRIC_PUB_KEY, MySqlBaseParser.CREATE_DH_PARAMETERS, MySqlBaseParser.CREATE_DIGEST, MySqlBaseParser.CROSSES, MySqlBaseParser.DATEDIFF, MySqlBaseParser.DATE_FORMAT, MySqlBaseParser.DAYNAME, MySqlBaseParser.DAYOFMONTH, MySqlBaseParser.DAYOFWEEK, MySqlBaseParser.DAYOFYEAR, MySqlBaseParser.DECODE, MySqlBaseParser.DEGREES, MySqlBaseParser.DES_DECRYPT, MySqlBaseParser.DES_ENCRYPT, MySqlBaseParser.DIMENSION, MySqlBaseParser.DISJOINT, MySqlBaseParser.ELT, MySqlBaseParser.ENCODE, MySqlBaseParser.ENCRYPT, MySqlBaseParser.ENDPOINT, MySqlBaseParser.ENVELOPE, MySqlBaseParser.EQUALS, MySqlBaseParser.EXP, MySqlBaseParser.EXPORT_SET, MySqlBaseParser.EXTERIORRING, MySqlBaseParser.EXTRACTVALUE, MySqlBaseParser.FIELD, MySqlBaseParser.FIND_IN_SET, MySqlBaseParser.FLOOR, MySqlBaseParser.FORMAT, MySqlBaseParser.FOUND_ROWS, MySqlBaseParser.FROM_BASE64, MySqlBaseParser.FROM_DAYS, MySqlBaseParser.FROM_UNIXTIME, MySqlBaseParser.GEOMCOLLFROMTEXT, MySqlBaseParser.GEOMCOLLFROMWKB, MySqlBaseParser.GEOMETRYCOLLECTIONFROMTEXT, MySqlBaseParser.GEOMETRYCOLLECTIONFROMWKB, MySqlBaseParser.GEOMETRYFROMTEXT, MySqlBaseParser.GEOMETRYFROMWKB, MySqlBaseParser.GEOMETRYN, MySqlBaseParser.GEOMETRYTYPE, MySqlBaseParser.GEOMFROMTEXT, MySqlBaseParser.GEOMFROMWKB, MySqlBaseParser.GET_FORMAT, MySqlBaseParser.GET_LOCK, MySqlBaseParser.GLENGTH, MySqlBaseParser.GREATEST, MySqlBaseParser.GTID_SUBSET, MySqlBaseParser.GTID_SUBTRACT, MySqlBaseParser.HEX, MySqlBaseParser.IFNULL, MySqlBaseParser.INET6_ATON, MySqlBaseParser.INET6_NTOA, MySqlBaseParser.INET_ATON, MySqlBaseParser.INET_NTOA, MySqlBaseParser.INSTR, MySqlBaseParser.INTERIORRINGN, MySqlBaseParser.INTERSECTS, MySqlBaseParser.ISCLOSED, MySqlBaseParser.ISEMPTY, MySqlBaseParser.ISNULL, MySqlBaseParser.ISSIMPLE, MySqlBaseParser.IS_FREE_LOCK, MySqlBaseParser.IS_IPV4, MySqlBaseParser.IS_IPV4_COMPAT, MySqlBaseParser.IS_IPV4_MAPPED, MySqlBaseParser.IS_IPV6, MySqlBaseParser.IS_USED_LOCK, MySqlBaseParser.LAST_INSERT_ID, MySqlBaseParser.LCASE, MySqlBaseParser.LEAST, MySqlBaseParser.LENGTH, MySqlBaseParser.LINEFROMTEXT, MySqlBaseParser.LINEFROMWKB, MySqlBaseParser.LINESTRINGFROMTEXT, MySqlBaseParser.LINESTRINGFROMWKB, MySqlBaseParser.LN, MySqlBaseParser.LOAD_FILE, MySqlBaseParser.LOCATE, MySqlBaseParser.LOG, MySqlBaseParser.LOG10, MySqlBaseParser.LOG2, MySqlBaseParser.LOWER, MySqlBaseParser.LPAD, MySqlBaseParser.LTRIM, MySqlBaseParser.MAKEDATE, MySqlBaseParser.MAKETIME, MySqlBaseParser.MAKE_SET, MySqlBaseParser.MASTER_POS_WAIT, MySqlBaseParser.MBRCONTAINS, MySqlBaseParser.MBRDISJOINT, MySqlBaseParser.MBREQUAL, MySqlBaseParser.MBRINTERSECTS, MySqlBaseParser.MBROVERLAPS, MySqlBaseParser.MBRTOUCHES, MySqlBaseParser.MBRWITHIN, MySqlBaseParser.MD5, MySqlBaseParser.MLINEFROMTEXT, MySqlBaseParser.MLINEFROMWKB, MySqlBaseParser.MONTHNAME, MySqlBaseParser.MPOINTFROMTEXT, MySqlBaseParser.MPOINTFROMWKB, MySqlBaseParser.MPOLYFROMTEXT, MySqlBaseParser.MPOLYFROMWKB, MySqlBaseParser.MULTILINESTRINGFROMTEXT, MySqlBaseParser.MULTILINESTRINGFROMWKB, MySqlBaseParser.MULTIPOINTFROMTEXT, MySqlBaseParser.MULTIPOINTFROMWKB, MySqlBaseParser.MULTIPOLYGONFROMTEXT, MySqlBaseParser.MULTIPOLYGONFROMWKB, MySqlBaseParser.NAME_CONST, MySqlBaseParser.NULLIF, MySqlBaseParser.NUMGEOMETRIES, MySqlBaseParser.NUMINTERIORRINGS, MySqlBaseParser.NUMPOINTS, MySqlBaseParser.OCT, MySqlBaseParser.OCTET_LENGTH, MySqlBaseParser.ORD, MySqlBaseParser.OVERLAPS, MySqlBaseParser.PERIOD_ADD, MySqlBaseParser.PERIOD_DIFF, MySqlBaseParser.PI, MySqlBaseParser.POINTFROMTEXT, MySqlBaseParser.POINTFROMWKB, MySqlBaseParser.POINTN, MySqlBaseParser.POLYFROMTEXT, MySqlBaseParser.POLYFROMWKB, MySqlBaseParser.POLYGONFROMTEXT, MySqlBaseParser.POLYGONFROMWKB, MySqlBaseParser.POW, MySqlBaseParser.POWER, MySqlBaseParser.QUOTE, MySqlBaseParser.RADIANS, MySqlBaseParser.RAND, MySqlBaseParser.RANDOM_BYTES, MySqlBaseParser.RELEASE_LOCK, MySqlBaseParser.REVERSE, MySqlBaseParser.ROUND, MySqlBaseParser.ROW_COUNT, MySqlBaseParser.RPAD, MySqlBaseParser.RTRIM, MySqlBaseParser.SEC_TO_TIME, MySqlBaseParser.SESSION_USER, MySqlBaseParser.SHA, MySqlBaseParser.SHA1, MySqlBaseParser.SHA2, MySqlBaseParser.SIGN, MySqlBaseParser.SIN, MySqlBaseParser.SLEEP, MySqlBaseParser.SOUNDEX, MySqlBaseParser.SQL_THREAD_WAIT_AFTER_GTIDS, MySqlBaseParser.SQRT, MySqlBaseParser.SRID, MySqlBaseParser.STARTPOINT, MySqlBaseParser.STRCMP, MySqlBaseParser.STR_TO_DATE, MySqlBaseParser.ST_AREA, MySqlBaseParser.ST_ASBINARY, MySqlBaseParser.ST_ASTEXT, MySqlBaseParser.ST_ASWKB, MySqlBaseParser.ST_ASWKT, MySqlBaseParser.ST_BUFFER, MySqlBaseParser.ST_CENTROID, MySqlBaseParser.ST_CONTAINS, MySqlBaseParser.ST_CROSSES, MySqlBaseParser.ST_DIFFERENCE, MySqlBaseParser.ST_DIMENSION, MySqlBaseParser.ST_DISJOINT, MySqlBaseParser.ST_DISTANCE, MySqlBaseParser.ST_ENDPOINT, MySqlBaseParser.ST_ENVELOPE, MySqlBaseParser.ST_EQUALS, MySqlBaseParser.ST_EXTERIORRING, MySqlBaseParser.ST_GEOMCOLLFROMTEXT, MySqlBaseParser.ST_GEOMCOLLFROMTXT, MySqlBaseParser.ST_GEOMCOLLFROMWKB, MySqlBaseParser.ST_GEOMETRYCOLLECTIONFROMTEXT, MySqlBaseParser.ST_GEOMETRYCOLLECTIONFROMWKB, MySqlBaseParser.ST_GEOMETRYFROMTEXT, MySqlBaseParser.ST_GEOMETRYFROMWKB, MySqlBaseParser.ST_GEOMETRYN, MySqlBaseParser.ST_GEOMETRYTYPE, MySqlBaseParser.ST_GEOMFROMTEXT, MySqlBaseParser.ST_GEOMFROMWKB, MySqlBaseParser.ST_INTERIORRINGN, MySqlBaseParser.ST_INTERSECTION, MySqlBaseParser.ST_INTERSECTS, MySqlBaseParser.ST_ISCLOSED, MySqlBaseParser.ST_ISEMPTY, MySqlBaseParser.ST_ISSIMPLE, MySqlBaseParser.ST_LINEFROMTEXT, MySqlBaseParser.ST_LINEFROMWKB, MySqlBaseParser.ST_LINESTRINGFROMTEXT, MySqlBaseParser.ST_LINESTRINGFROMWKB, MySqlBaseParser.ST_NUMGEOMETRIES, MySqlBaseParser.ST_NUMINTERIORRING, MySqlBaseParser.ST_NUMINTERIORRINGS, MySqlBaseParser.ST_NUMPOINTS, MySqlBaseParser.ST_OVERLAPS, MySqlBaseParser.ST_POINTFROMTEXT, MySqlBaseParser.ST_POINTFROMWKB, MySqlBaseParser.ST_POINTN, MySqlBaseParser.ST_POLYFROMTEXT, MySqlBaseParser.ST_POLYFROMWKB, MySqlBaseParser.ST_POLYGONFROMTEXT, MySqlBaseParser.ST_POLYGONFROMWKB, MySqlBaseParser.ST_SRID, MySqlBaseParser.ST_STARTPOINT, MySqlBaseParser.ST_SYMDIFFERENCE, MySqlBaseParser.ST_TOUCHES, MySqlBaseParser.ST_UNION, MySqlBaseParser.ST_WITHIN, MySqlBaseParser.ST_X, MySqlBaseParser.ST_Y, MySqlBaseParser.SUBDATE, MySqlBaseParser.SUBSTRING_INDEX, MySqlBaseParser.SUBTIME, MySqlBaseParser.SYSTEM_USER, MySqlBaseParser.TAN, MySqlBaseParser.TIMEDIFF, MySqlBaseParser.TIMESTAMPADD, MySqlBaseParser.TIMESTAMPDIFF, MySqlBaseParser.TIME_FORMAT, MySqlBaseParser.TIME_TO_SEC, MySqlBaseParser.TOUCHES, MySqlBaseParser.TO_BASE64, MySqlBaseParser.TO_DAYS, MySqlBaseParser.TO_SECONDS, MySqlBaseParser.UCASE, MySqlBaseParser.UNCOMPRESS, MySqlBaseParser.UNCOMPRESSED_LENGTH, MySqlBaseParser.UNHEX, MySqlBaseParser.UNIX_TIMESTAMP, MySqlBaseParser.UPDATEXML, MySqlBaseParser.UPPER, MySqlBaseParser.UUID, MySqlBaseParser.UUID_SHORT, MySqlBaseParser.VALIDATE_PASSWORD_STRENGTH, MySqlBaseParser.VERSION, MySqlBaseParser.WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS, MySqlBaseParser.WEEKDAY, MySqlBaseParser.WEEKOFYEAR, MySqlBaseParser.WEIGHT_STRING, MySqlBaseParser.WITHIN, MySqlBaseParser.YEARWEEK, MySqlBaseParser.Y_FUNCTION, MySqlBaseParser.X_FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.functionNameBase()
                pass
            elif token in [MySqlBaseParser.ASCII]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(MySqlBaseParser.ASCII)
                pass
            elif token in [MySqlBaseParser.CURDATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.match(MySqlBaseParser.CURDATE)
                pass
            elif token in [MySqlBaseParser.CURRENT_DATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 380
                self.match(MySqlBaseParser.CURRENT_DATE)
                pass
            elif token in [MySqlBaseParser.CURRENT_TIME]:
                self.enterOuterAlt(localctx, 5)
                self.state = 381
                self.match(MySqlBaseParser.CURRENT_TIME)
                pass
            elif token in [MySqlBaseParser.CURRENT_TIMESTAMP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 382
                self.match(MySqlBaseParser.CURRENT_TIMESTAMP)
                pass
            elif token in [MySqlBaseParser.CURTIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 383
                self.match(MySqlBaseParser.CURTIME)
                pass
            elif token in [MySqlBaseParser.DATE_ADD]:
                self.enterOuterAlt(localctx, 8)
                self.state = 384
                self.match(MySqlBaseParser.DATE_ADD)
                pass
            elif token in [MySqlBaseParser.DATE_SUB]:
                self.enterOuterAlt(localctx, 9)
                self.state = 385
                self.match(MySqlBaseParser.DATE_SUB)
                pass
            elif token in [MySqlBaseParser.IF]:
                self.enterOuterAlt(localctx, 10)
                self.state = 386
                self.match(MySqlBaseParser.IF)
                pass
            elif token in [MySqlBaseParser.INSERT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 387
                self.match(MySqlBaseParser.INSERT)
                pass
            elif token in [MySqlBaseParser.LOCALTIME]:
                self.enterOuterAlt(localctx, 12)
                self.state = 388
                self.match(MySqlBaseParser.LOCALTIME)
                pass
            elif token in [MySqlBaseParser.LOCALTIMESTAMP]:
                self.enterOuterAlt(localctx, 13)
                self.state = 389
                self.match(MySqlBaseParser.LOCALTIMESTAMP)
                pass
            elif token in [MySqlBaseParser.MID]:
                self.enterOuterAlt(localctx, 14)
                self.state = 390
                self.match(MySqlBaseParser.MID)
                pass
            elif token in [MySqlBaseParser.NOW]:
                self.enterOuterAlt(localctx, 15)
                self.state = 391
                self.match(MySqlBaseParser.NOW)
                pass
            elif token in [MySqlBaseParser.REPLACE]:
                self.enterOuterAlt(localctx, 16)
                self.state = 392
                self.match(MySqlBaseParser.REPLACE)
                pass
            elif token in [MySqlBaseParser.SUBSTR]:
                self.enterOuterAlt(localctx, 17)
                self.state = 393
                self.match(MySqlBaseParser.SUBSTR)
                pass
            elif token in [MySqlBaseParser.SUBSTRING]:
                self.enterOuterAlt(localctx, 18)
                self.state = 394
                self.match(MySqlBaseParser.SUBSTRING)
                pass
            elif token in [MySqlBaseParser.SYSDATE]:
                self.enterOuterAlt(localctx, 19)
                self.state = 395
                self.match(MySqlBaseParser.SYSDATE)
                pass
            elif token in [MySqlBaseParser.TRIM]:
                self.enterOuterAlt(localctx, 20)
                self.state = 396
                self.match(MySqlBaseParser.TRIM)
                pass
            elif token in [MySqlBaseParser.UTC_DATE]:
                self.enterOuterAlt(localctx, 21)
                self.state = 397
                self.match(MySqlBaseParser.UTC_DATE)
                pass
            elif token in [MySqlBaseParser.UTC_TIME]:
                self.enterOuterAlt(localctx, 22)
                self.state = 398
                self.match(MySqlBaseParser.UTC_TIME)
                pass
            elif token in [MySqlBaseParser.UTC_TIMESTAMP]:
                self.enterOuterAlt(localctx, 23)
                self.state = 399
                self.match(MySqlBaseParser.UTC_TIMESTAMP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_specificFunction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleFunctionCallContext(SpecificFunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlBaseParser.SpecificFunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CURRENT_DATE(self):
            return self.getToken(MySqlBaseParser.CURRENT_DATE, 0)
        def CURRENT_TIME(self):
            return self.getToken(MySqlBaseParser.CURRENT_TIME, 0)
        def CURRENT_TIMESTAMP(self):
            return self.getToken(MySqlBaseParser.CURRENT_TIMESTAMP, 0)
        def CURRENT_USER(self):
            return self.getToken(MySqlBaseParser.CURRENT_USER, 0)
        def LOCALTIME(self):
            return self.getToken(MySqlBaseParser.LOCALTIME, 0)
        def LR_BRACKET(self):
            return self.getToken(MySqlBaseParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(MySqlBaseParser.RR_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleFunctionCall" ):
                listener.enterSimpleFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleFunctionCall" ):
                listener.exitSimpleFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleFunctionCall" ):
                return visitor.visitSimpleFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def specificFunction(self):

        localctx = MySqlBaseParser.SpecificFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_specificFunction)
        self._la = 0 # Token type
        try:
            localctx = MySqlBaseParser.SimpleFunctionCallContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            _la = self._input.LA(1)
            if not(_la==MySqlBaseParser.CURRENT_USER or ((((_la - 326)) & ~0x3f) == 0 and ((1 << (_la - 326)) & ((1 << (MySqlBaseParser.CURRENT_DATE - 326)) | (1 << (MySqlBaseParser.CURRENT_TIME - 326)) | (1 << (MySqlBaseParser.CURRENT_TIMESTAMP - 326)) | (1 << (MySqlBaseParser.LOCALTIME - 326)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 403
                self.match(MySqlBaseParser.LR_BRACKET)
                self.state = 404
                self.match(MySqlBaseParser.RR_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.FunctionArgContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.FunctionArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.COMMA)
            else:
                return self.getToken(MySqlBaseParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_functionArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgs" ):
                listener.enterFunctionArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgs" ):
                listener.exitFunctionArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgs" ):
                return visitor.visitFunctionArgs(self)
            else:
                return visitor.visitChildren(self)




    def functionArgs(self):

        localctx = MySqlBaseParser.FunctionArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.functionArg()
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlBaseParser.COMMA:
                self.state = 408
                self.match(MySqlBaseParser.COMMA)
                self.state = 409
                self.functionArg()
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(MySqlBaseParser.ConstantContext,0)


        def fullColumnName(self):
            return self.getTypedRuleContext(MySqlBaseParser.FullColumnNameContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MySqlBaseParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_functionArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArg" ):
                listener.enterFunctionArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArg" ):
                listener.exitFunctionArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArg" ):
                return visitor.visitFunctionArg(self)
            else:
                return visitor.visitChildren(self)




    def functionArg(self):

        localctx = MySqlBaseParser.FunctionArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functionArg)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.fullColumnName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameBaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABS(self):
            return self.getToken(MySqlBaseParser.ABS, 0)

        def ACOS(self):
            return self.getToken(MySqlBaseParser.ACOS, 0)

        def ADDDATE(self):
            return self.getToken(MySqlBaseParser.ADDDATE, 0)

        def ADDTIME(self):
            return self.getToken(MySqlBaseParser.ADDTIME, 0)

        def AES_DECRYPT(self):
            return self.getToken(MySqlBaseParser.AES_DECRYPT, 0)

        def AES_ENCRYPT(self):
            return self.getToken(MySqlBaseParser.AES_ENCRYPT, 0)

        def AREA(self):
            return self.getToken(MySqlBaseParser.AREA, 0)

        def ASBINARY(self):
            return self.getToken(MySqlBaseParser.ASBINARY, 0)

        def ASIN(self):
            return self.getToken(MySqlBaseParser.ASIN, 0)

        def ASTEXT(self):
            return self.getToken(MySqlBaseParser.ASTEXT, 0)

        def ASWKB(self):
            return self.getToken(MySqlBaseParser.ASWKB, 0)

        def ASWKT(self):
            return self.getToken(MySqlBaseParser.ASWKT, 0)

        def ASYMMETRIC_DECRYPT(self):
            return self.getToken(MySqlBaseParser.ASYMMETRIC_DECRYPT, 0)

        def ASYMMETRIC_DERIVE(self):
            return self.getToken(MySqlBaseParser.ASYMMETRIC_DERIVE, 0)

        def ASYMMETRIC_ENCRYPT(self):
            return self.getToken(MySqlBaseParser.ASYMMETRIC_ENCRYPT, 0)

        def ASYMMETRIC_SIGN(self):
            return self.getToken(MySqlBaseParser.ASYMMETRIC_SIGN, 0)

        def ASYMMETRIC_VERIFY(self):
            return self.getToken(MySqlBaseParser.ASYMMETRIC_VERIFY, 0)

        def ATAN(self):
            return self.getToken(MySqlBaseParser.ATAN, 0)

        def ATAN2(self):
            return self.getToken(MySqlBaseParser.ATAN2, 0)

        def BENCHMARK(self):
            return self.getToken(MySqlBaseParser.BENCHMARK, 0)

        def BIN(self):
            return self.getToken(MySqlBaseParser.BIN, 0)

        def BIT_COUNT(self):
            return self.getToken(MySqlBaseParser.BIT_COUNT, 0)

        def BIT_LENGTH(self):
            return self.getToken(MySqlBaseParser.BIT_LENGTH, 0)

        def BUFFER(self):
            return self.getToken(MySqlBaseParser.BUFFER, 0)

        def CEIL(self):
            return self.getToken(MySqlBaseParser.CEIL, 0)

        def CEILING(self):
            return self.getToken(MySqlBaseParser.CEILING, 0)

        def CENTROID(self):
            return self.getToken(MySqlBaseParser.CENTROID, 0)

        def CHARACTER_LENGTH(self):
            return self.getToken(MySqlBaseParser.CHARACTER_LENGTH, 0)

        def CHARSET(self):
            return self.getToken(MySqlBaseParser.CHARSET, 0)

        def CHAR_LENGTH(self):
            return self.getToken(MySqlBaseParser.CHAR_LENGTH, 0)

        def COERCIBILITY(self):
            return self.getToken(MySqlBaseParser.COERCIBILITY, 0)

        def COLLATION(self):
            return self.getToken(MySqlBaseParser.COLLATION, 0)

        def COMPRESS(self):
            return self.getToken(MySqlBaseParser.COMPRESS, 0)

        def CONCAT(self):
            return self.getToken(MySqlBaseParser.CONCAT, 0)

        def CONCAT_WS(self):
            return self.getToken(MySqlBaseParser.CONCAT_WS, 0)

        def CONNECTION_ID(self):
            return self.getToken(MySqlBaseParser.CONNECTION_ID, 0)

        def CONV(self):
            return self.getToken(MySqlBaseParser.CONV, 0)

        def CONVERT_TZ(self):
            return self.getToken(MySqlBaseParser.CONVERT_TZ, 0)

        def COS(self):
            return self.getToken(MySqlBaseParser.COS, 0)

        def COT(self):
            return self.getToken(MySqlBaseParser.COT, 0)

        def COUNT(self):
            return self.getToken(MySqlBaseParser.COUNT, 0)

        def CRC32(self):
            return self.getToken(MySqlBaseParser.CRC32, 0)

        def CREATE_ASYMMETRIC_PRIV_KEY(self):
            return self.getToken(MySqlBaseParser.CREATE_ASYMMETRIC_PRIV_KEY, 0)

        def CREATE_ASYMMETRIC_PUB_KEY(self):
            return self.getToken(MySqlBaseParser.CREATE_ASYMMETRIC_PUB_KEY, 0)

        def CREATE_DH_PARAMETERS(self):
            return self.getToken(MySqlBaseParser.CREATE_DH_PARAMETERS, 0)

        def CREATE_DIGEST(self):
            return self.getToken(MySqlBaseParser.CREATE_DIGEST, 0)

        def CROSSES(self):
            return self.getToken(MySqlBaseParser.CROSSES, 0)

        def DATABASE(self):
            return self.getToken(MySqlBaseParser.DATABASE, 0)

        def DATE(self):
            return self.getToken(MySqlBaseParser.DATE, 0)

        def DATEDIFF(self):
            return self.getToken(MySqlBaseParser.DATEDIFF, 0)

        def DATE_FORMAT(self):
            return self.getToken(MySqlBaseParser.DATE_FORMAT, 0)

        def DAY(self):
            return self.getToken(MySqlBaseParser.DAY, 0)

        def DAYNAME(self):
            return self.getToken(MySqlBaseParser.DAYNAME, 0)

        def DAYOFMONTH(self):
            return self.getToken(MySqlBaseParser.DAYOFMONTH, 0)

        def DAYOFWEEK(self):
            return self.getToken(MySqlBaseParser.DAYOFWEEK, 0)

        def DAYOFYEAR(self):
            return self.getToken(MySqlBaseParser.DAYOFYEAR, 0)

        def DECODE(self):
            return self.getToken(MySqlBaseParser.DECODE, 0)

        def DEGREES(self):
            return self.getToken(MySqlBaseParser.DEGREES, 0)

        def DES_DECRYPT(self):
            return self.getToken(MySqlBaseParser.DES_DECRYPT, 0)

        def DES_ENCRYPT(self):
            return self.getToken(MySqlBaseParser.DES_ENCRYPT, 0)

        def DIMENSION(self):
            return self.getToken(MySqlBaseParser.DIMENSION, 0)

        def DISJOINT(self):
            return self.getToken(MySqlBaseParser.DISJOINT, 0)

        def ELT(self):
            return self.getToken(MySqlBaseParser.ELT, 0)

        def ENCODE(self):
            return self.getToken(MySqlBaseParser.ENCODE, 0)

        def ENCRYPT(self):
            return self.getToken(MySqlBaseParser.ENCRYPT, 0)

        def ENDPOINT(self):
            return self.getToken(MySqlBaseParser.ENDPOINT, 0)

        def ENVELOPE(self):
            return self.getToken(MySqlBaseParser.ENVELOPE, 0)

        def EQUALS(self):
            return self.getToken(MySqlBaseParser.EQUALS, 0)

        def EXP(self):
            return self.getToken(MySqlBaseParser.EXP, 0)

        def EXPORT_SET(self):
            return self.getToken(MySqlBaseParser.EXPORT_SET, 0)

        def EXTERIORRING(self):
            return self.getToken(MySqlBaseParser.EXTERIORRING, 0)

        def EXTRACTVALUE(self):
            return self.getToken(MySqlBaseParser.EXTRACTVALUE, 0)

        def FIELD(self):
            return self.getToken(MySqlBaseParser.FIELD, 0)

        def FIND_IN_SET(self):
            return self.getToken(MySqlBaseParser.FIND_IN_SET, 0)

        def FLOOR(self):
            return self.getToken(MySqlBaseParser.FLOOR, 0)

        def FORMAT(self):
            return self.getToken(MySqlBaseParser.FORMAT, 0)

        def FOUND_ROWS(self):
            return self.getToken(MySqlBaseParser.FOUND_ROWS, 0)

        def FROM_BASE64(self):
            return self.getToken(MySqlBaseParser.FROM_BASE64, 0)

        def FROM_DAYS(self):
            return self.getToken(MySqlBaseParser.FROM_DAYS, 0)

        def FROM_UNIXTIME(self):
            return self.getToken(MySqlBaseParser.FROM_UNIXTIME, 0)

        def GEOMCOLLFROMTEXT(self):
            return self.getToken(MySqlBaseParser.GEOMCOLLFROMTEXT, 0)

        def GEOMCOLLFROMWKB(self):
            return self.getToken(MySqlBaseParser.GEOMCOLLFROMWKB, 0)

        def GEOMETRYCOLLECTION(self):
            return self.getToken(MySqlBaseParser.GEOMETRYCOLLECTION, 0)

        def GEOMETRYCOLLECTIONFROMTEXT(self):
            return self.getToken(MySqlBaseParser.GEOMETRYCOLLECTIONFROMTEXT, 0)

        def GEOMETRYCOLLECTIONFROMWKB(self):
            return self.getToken(MySqlBaseParser.GEOMETRYCOLLECTIONFROMWKB, 0)

        def GEOMETRYFROMTEXT(self):
            return self.getToken(MySqlBaseParser.GEOMETRYFROMTEXT, 0)

        def GEOMETRYFROMWKB(self):
            return self.getToken(MySqlBaseParser.GEOMETRYFROMWKB, 0)

        def GEOMETRYN(self):
            return self.getToken(MySqlBaseParser.GEOMETRYN, 0)

        def GEOMETRYTYPE(self):
            return self.getToken(MySqlBaseParser.GEOMETRYTYPE, 0)

        def GEOMFROMTEXT(self):
            return self.getToken(MySqlBaseParser.GEOMFROMTEXT, 0)

        def GEOMFROMWKB(self):
            return self.getToken(MySqlBaseParser.GEOMFROMWKB, 0)

        def GET_FORMAT(self):
            return self.getToken(MySqlBaseParser.GET_FORMAT, 0)

        def GET_LOCK(self):
            return self.getToken(MySqlBaseParser.GET_LOCK, 0)

        def GLENGTH(self):
            return self.getToken(MySqlBaseParser.GLENGTH, 0)

        def GREATEST(self):
            return self.getToken(MySqlBaseParser.GREATEST, 0)

        def GTID_SUBSET(self):
            return self.getToken(MySqlBaseParser.GTID_SUBSET, 0)

        def GTID_SUBTRACT(self):
            return self.getToken(MySqlBaseParser.GTID_SUBTRACT, 0)

        def HEX(self):
            return self.getToken(MySqlBaseParser.HEX, 0)

        def HOUR(self):
            return self.getToken(MySqlBaseParser.HOUR, 0)

        def IFNULL(self):
            return self.getToken(MySqlBaseParser.IFNULL, 0)

        def INET6_ATON(self):
            return self.getToken(MySqlBaseParser.INET6_ATON, 0)

        def INET6_NTOA(self):
            return self.getToken(MySqlBaseParser.INET6_NTOA, 0)

        def INET_ATON(self):
            return self.getToken(MySqlBaseParser.INET_ATON, 0)

        def INET_NTOA(self):
            return self.getToken(MySqlBaseParser.INET_NTOA, 0)

        def INSTR(self):
            return self.getToken(MySqlBaseParser.INSTR, 0)

        def INTERIORRINGN(self):
            return self.getToken(MySqlBaseParser.INTERIORRINGN, 0)

        def INTERSECTS(self):
            return self.getToken(MySqlBaseParser.INTERSECTS, 0)

        def INVISIBLE(self):
            return self.getToken(MySqlBaseParser.INVISIBLE, 0)

        def ISCLOSED(self):
            return self.getToken(MySqlBaseParser.ISCLOSED, 0)

        def ISEMPTY(self):
            return self.getToken(MySqlBaseParser.ISEMPTY, 0)

        def ISNULL(self):
            return self.getToken(MySqlBaseParser.ISNULL, 0)

        def ISSIMPLE(self):
            return self.getToken(MySqlBaseParser.ISSIMPLE, 0)

        def IS_FREE_LOCK(self):
            return self.getToken(MySqlBaseParser.IS_FREE_LOCK, 0)

        def IS_IPV4(self):
            return self.getToken(MySqlBaseParser.IS_IPV4, 0)

        def IS_IPV4_COMPAT(self):
            return self.getToken(MySqlBaseParser.IS_IPV4_COMPAT, 0)

        def IS_IPV4_MAPPED(self):
            return self.getToken(MySqlBaseParser.IS_IPV4_MAPPED, 0)

        def IS_IPV6(self):
            return self.getToken(MySqlBaseParser.IS_IPV6, 0)

        def IS_USED_LOCK(self):
            return self.getToken(MySqlBaseParser.IS_USED_LOCK, 0)

        def LAST_INSERT_ID(self):
            return self.getToken(MySqlBaseParser.LAST_INSERT_ID, 0)

        def LCASE(self):
            return self.getToken(MySqlBaseParser.LCASE, 0)

        def LEAST(self):
            return self.getToken(MySqlBaseParser.LEAST, 0)

        def LEFT(self):
            return self.getToken(MySqlBaseParser.LEFT, 0)

        def LENGTH(self):
            return self.getToken(MySqlBaseParser.LENGTH, 0)

        def LINEFROMTEXT(self):
            return self.getToken(MySqlBaseParser.LINEFROMTEXT, 0)

        def LINEFROMWKB(self):
            return self.getToken(MySqlBaseParser.LINEFROMWKB, 0)

        def LINESTRING(self):
            return self.getToken(MySqlBaseParser.LINESTRING, 0)

        def LINESTRINGFROMTEXT(self):
            return self.getToken(MySqlBaseParser.LINESTRINGFROMTEXT, 0)

        def LINESTRINGFROMWKB(self):
            return self.getToken(MySqlBaseParser.LINESTRINGFROMWKB, 0)

        def LN(self):
            return self.getToken(MySqlBaseParser.LN, 0)

        def LOAD_FILE(self):
            return self.getToken(MySqlBaseParser.LOAD_FILE, 0)

        def LOCATE(self):
            return self.getToken(MySqlBaseParser.LOCATE, 0)

        def LOG(self):
            return self.getToken(MySqlBaseParser.LOG, 0)

        def LOG10(self):
            return self.getToken(MySqlBaseParser.LOG10, 0)

        def LOG2(self):
            return self.getToken(MySqlBaseParser.LOG2, 0)

        def LOWER(self):
            return self.getToken(MySqlBaseParser.LOWER, 0)

        def LPAD(self):
            return self.getToken(MySqlBaseParser.LPAD, 0)

        def LTRIM(self):
            return self.getToken(MySqlBaseParser.LTRIM, 0)

        def MAKEDATE(self):
            return self.getToken(MySqlBaseParser.MAKEDATE, 0)

        def MAKETIME(self):
            return self.getToken(MySqlBaseParser.MAKETIME, 0)

        def MAKE_SET(self):
            return self.getToken(MySqlBaseParser.MAKE_SET, 0)

        def MASTER_POS_WAIT(self):
            return self.getToken(MySqlBaseParser.MASTER_POS_WAIT, 0)

        def MBRCONTAINS(self):
            return self.getToken(MySqlBaseParser.MBRCONTAINS, 0)

        def MBRDISJOINT(self):
            return self.getToken(MySqlBaseParser.MBRDISJOINT, 0)

        def MBREQUAL(self):
            return self.getToken(MySqlBaseParser.MBREQUAL, 0)

        def MBRINTERSECTS(self):
            return self.getToken(MySqlBaseParser.MBRINTERSECTS, 0)

        def MBROVERLAPS(self):
            return self.getToken(MySqlBaseParser.MBROVERLAPS, 0)

        def MBRTOUCHES(self):
            return self.getToken(MySqlBaseParser.MBRTOUCHES, 0)

        def MBRWITHIN(self):
            return self.getToken(MySqlBaseParser.MBRWITHIN, 0)

        def MD5(self):
            return self.getToken(MySqlBaseParser.MD5, 0)

        def MICROSECOND(self):
            return self.getToken(MySqlBaseParser.MICROSECOND, 0)

        def MINUTE(self):
            return self.getToken(MySqlBaseParser.MINUTE, 0)

        def MLINEFROMTEXT(self):
            return self.getToken(MySqlBaseParser.MLINEFROMTEXT, 0)

        def MLINEFROMWKB(self):
            return self.getToken(MySqlBaseParser.MLINEFROMWKB, 0)

        def MOD(self):
            return self.getToken(MySqlBaseParser.MOD, 0)

        def MONTH(self):
            return self.getToken(MySqlBaseParser.MONTH, 0)

        def MONTHNAME(self):
            return self.getToken(MySqlBaseParser.MONTHNAME, 0)

        def MPOINTFROMTEXT(self):
            return self.getToken(MySqlBaseParser.MPOINTFROMTEXT, 0)

        def MPOINTFROMWKB(self):
            return self.getToken(MySqlBaseParser.MPOINTFROMWKB, 0)

        def MPOLYFROMTEXT(self):
            return self.getToken(MySqlBaseParser.MPOLYFROMTEXT, 0)

        def MPOLYFROMWKB(self):
            return self.getToken(MySqlBaseParser.MPOLYFROMWKB, 0)

        def MULTILINESTRING(self):
            return self.getToken(MySqlBaseParser.MULTILINESTRING, 0)

        def MULTILINESTRINGFROMTEXT(self):
            return self.getToken(MySqlBaseParser.MULTILINESTRINGFROMTEXT, 0)

        def MULTILINESTRINGFROMWKB(self):
            return self.getToken(MySqlBaseParser.MULTILINESTRINGFROMWKB, 0)

        def MULTIPOINT(self):
            return self.getToken(MySqlBaseParser.MULTIPOINT, 0)

        def MULTIPOINTFROMTEXT(self):
            return self.getToken(MySqlBaseParser.MULTIPOINTFROMTEXT, 0)

        def MULTIPOINTFROMWKB(self):
            return self.getToken(MySqlBaseParser.MULTIPOINTFROMWKB, 0)

        def MULTIPOLYGON(self):
            return self.getToken(MySqlBaseParser.MULTIPOLYGON, 0)

        def MULTIPOLYGONFROMTEXT(self):
            return self.getToken(MySqlBaseParser.MULTIPOLYGONFROMTEXT, 0)

        def MULTIPOLYGONFROMWKB(self):
            return self.getToken(MySqlBaseParser.MULTIPOLYGONFROMWKB, 0)

        def NAME_CONST(self):
            return self.getToken(MySqlBaseParser.NAME_CONST, 0)

        def NULLIF(self):
            return self.getToken(MySqlBaseParser.NULLIF, 0)

        def NUMGEOMETRIES(self):
            return self.getToken(MySqlBaseParser.NUMGEOMETRIES, 0)

        def NUMINTERIORRINGS(self):
            return self.getToken(MySqlBaseParser.NUMINTERIORRINGS, 0)

        def NUMPOINTS(self):
            return self.getToken(MySqlBaseParser.NUMPOINTS, 0)

        def OCT(self):
            return self.getToken(MySqlBaseParser.OCT, 0)

        def OCTET_LENGTH(self):
            return self.getToken(MySqlBaseParser.OCTET_LENGTH, 0)

        def ORD(self):
            return self.getToken(MySqlBaseParser.ORD, 0)

        def OVERLAPS(self):
            return self.getToken(MySqlBaseParser.OVERLAPS, 0)

        def PERIOD_ADD(self):
            return self.getToken(MySqlBaseParser.PERIOD_ADD, 0)

        def PERIOD_DIFF(self):
            return self.getToken(MySqlBaseParser.PERIOD_DIFF, 0)

        def PI(self):
            return self.getToken(MySqlBaseParser.PI, 0)

        def POINT(self):
            return self.getToken(MySqlBaseParser.POINT, 0)

        def POINTFROMTEXT(self):
            return self.getToken(MySqlBaseParser.POINTFROMTEXT, 0)

        def POINTFROMWKB(self):
            return self.getToken(MySqlBaseParser.POINTFROMWKB, 0)

        def POINTN(self):
            return self.getToken(MySqlBaseParser.POINTN, 0)

        def POLYFROMTEXT(self):
            return self.getToken(MySqlBaseParser.POLYFROMTEXT, 0)

        def POLYFROMWKB(self):
            return self.getToken(MySqlBaseParser.POLYFROMWKB, 0)

        def POLYGON(self):
            return self.getToken(MySqlBaseParser.POLYGON, 0)

        def POLYGONFROMTEXT(self):
            return self.getToken(MySqlBaseParser.POLYGONFROMTEXT, 0)

        def POLYGONFROMWKB(self):
            return self.getToken(MySqlBaseParser.POLYGONFROMWKB, 0)

        def POSITION(self):
            return self.getToken(MySqlBaseParser.POSITION, 0)

        def POW(self):
            return self.getToken(MySqlBaseParser.POW, 0)

        def POWER(self):
            return self.getToken(MySqlBaseParser.POWER, 0)

        def QUARTER(self):
            return self.getToken(MySqlBaseParser.QUARTER, 0)

        def QUOTE(self):
            return self.getToken(MySqlBaseParser.QUOTE, 0)

        def RADIANS(self):
            return self.getToken(MySqlBaseParser.RADIANS, 0)

        def RAND(self):
            return self.getToken(MySqlBaseParser.RAND, 0)

        def RANDOM_BYTES(self):
            return self.getToken(MySqlBaseParser.RANDOM_BYTES, 0)

        def RELEASE_LOCK(self):
            return self.getToken(MySqlBaseParser.RELEASE_LOCK, 0)

        def REVERSE(self):
            return self.getToken(MySqlBaseParser.REVERSE, 0)

        def RIGHT(self):
            return self.getToken(MySqlBaseParser.RIGHT, 0)

        def ROUND(self):
            return self.getToken(MySqlBaseParser.ROUND, 0)

        def ROW_COUNT(self):
            return self.getToken(MySqlBaseParser.ROW_COUNT, 0)

        def RPAD(self):
            return self.getToken(MySqlBaseParser.RPAD, 0)

        def RTRIM(self):
            return self.getToken(MySqlBaseParser.RTRIM, 0)

        def SECOND(self):
            return self.getToken(MySqlBaseParser.SECOND, 0)

        def SEC_TO_TIME(self):
            return self.getToken(MySqlBaseParser.SEC_TO_TIME, 0)

        def SCHEMA(self):
            return self.getToken(MySqlBaseParser.SCHEMA, 0)

        def SESSION_USER(self):
            return self.getToken(MySqlBaseParser.SESSION_USER, 0)

        def SESSION_VARIABLES_ADMIN(self):
            return self.getToken(MySqlBaseParser.SESSION_VARIABLES_ADMIN, 0)

        def SHA(self):
            return self.getToken(MySqlBaseParser.SHA, 0)

        def SHA1(self):
            return self.getToken(MySqlBaseParser.SHA1, 0)

        def SHA2(self):
            return self.getToken(MySqlBaseParser.SHA2, 0)

        def SIGN(self):
            return self.getToken(MySqlBaseParser.SIGN, 0)

        def SIN(self):
            return self.getToken(MySqlBaseParser.SIN, 0)

        def SLEEP(self):
            return self.getToken(MySqlBaseParser.SLEEP, 0)

        def SOUNDEX(self):
            return self.getToken(MySqlBaseParser.SOUNDEX, 0)

        def SQL_THREAD_WAIT_AFTER_GTIDS(self):
            return self.getToken(MySqlBaseParser.SQL_THREAD_WAIT_AFTER_GTIDS, 0)

        def SQRT(self):
            return self.getToken(MySqlBaseParser.SQRT, 0)

        def SRID(self):
            return self.getToken(MySqlBaseParser.SRID, 0)

        def STARTPOINT(self):
            return self.getToken(MySqlBaseParser.STARTPOINT, 0)

        def STRCMP(self):
            return self.getToken(MySqlBaseParser.STRCMP, 0)

        def STR_TO_DATE(self):
            return self.getToken(MySqlBaseParser.STR_TO_DATE, 0)

        def ST_AREA(self):
            return self.getToken(MySqlBaseParser.ST_AREA, 0)

        def ST_ASBINARY(self):
            return self.getToken(MySqlBaseParser.ST_ASBINARY, 0)

        def ST_ASTEXT(self):
            return self.getToken(MySqlBaseParser.ST_ASTEXT, 0)

        def ST_ASWKB(self):
            return self.getToken(MySqlBaseParser.ST_ASWKB, 0)

        def ST_ASWKT(self):
            return self.getToken(MySqlBaseParser.ST_ASWKT, 0)

        def ST_BUFFER(self):
            return self.getToken(MySqlBaseParser.ST_BUFFER, 0)

        def ST_CENTROID(self):
            return self.getToken(MySqlBaseParser.ST_CENTROID, 0)

        def ST_CONTAINS(self):
            return self.getToken(MySqlBaseParser.ST_CONTAINS, 0)

        def ST_CROSSES(self):
            return self.getToken(MySqlBaseParser.ST_CROSSES, 0)

        def ST_DIFFERENCE(self):
            return self.getToken(MySqlBaseParser.ST_DIFFERENCE, 0)

        def ST_DIMENSION(self):
            return self.getToken(MySqlBaseParser.ST_DIMENSION, 0)

        def ST_DISJOINT(self):
            return self.getToken(MySqlBaseParser.ST_DISJOINT, 0)

        def ST_DISTANCE(self):
            return self.getToken(MySqlBaseParser.ST_DISTANCE, 0)

        def ST_ENDPOINT(self):
            return self.getToken(MySqlBaseParser.ST_ENDPOINT, 0)

        def ST_ENVELOPE(self):
            return self.getToken(MySqlBaseParser.ST_ENVELOPE, 0)

        def ST_EQUALS(self):
            return self.getToken(MySqlBaseParser.ST_EQUALS, 0)

        def ST_EXTERIORRING(self):
            return self.getToken(MySqlBaseParser.ST_EXTERIORRING, 0)

        def ST_GEOMCOLLFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_GEOMCOLLFROMTEXT, 0)

        def ST_GEOMCOLLFROMTXT(self):
            return self.getToken(MySqlBaseParser.ST_GEOMCOLLFROMTXT, 0)

        def ST_GEOMCOLLFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_GEOMCOLLFROMWKB, 0)

        def ST_GEOMETRYCOLLECTIONFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_GEOMETRYCOLLECTIONFROMTEXT, 0)

        def ST_GEOMETRYCOLLECTIONFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_GEOMETRYCOLLECTIONFROMWKB, 0)

        def ST_GEOMETRYFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_GEOMETRYFROMTEXT, 0)

        def ST_GEOMETRYFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_GEOMETRYFROMWKB, 0)

        def ST_GEOMETRYN(self):
            return self.getToken(MySqlBaseParser.ST_GEOMETRYN, 0)

        def ST_GEOMETRYTYPE(self):
            return self.getToken(MySqlBaseParser.ST_GEOMETRYTYPE, 0)

        def ST_GEOMFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_GEOMFROMTEXT, 0)

        def ST_GEOMFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_GEOMFROMWKB, 0)

        def ST_INTERIORRINGN(self):
            return self.getToken(MySqlBaseParser.ST_INTERIORRINGN, 0)

        def ST_INTERSECTION(self):
            return self.getToken(MySqlBaseParser.ST_INTERSECTION, 0)

        def ST_INTERSECTS(self):
            return self.getToken(MySqlBaseParser.ST_INTERSECTS, 0)

        def ST_ISCLOSED(self):
            return self.getToken(MySqlBaseParser.ST_ISCLOSED, 0)

        def ST_ISEMPTY(self):
            return self.getToken(MySqlBaseParser.ST_ISEMPTY, 0)

        def ST_ISSIMPLE(self):
            return self.getToken(MySqlBaseParser.ST_ISSIMPLE, 0)

        def ST_LINEFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_LINEFROMTEXT, 0)

        def ST_LINEFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_LINEFROMWKB, 0)

        def ST_LINESTRINGFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_LINESTRINGFROMTEXT, 0)

        def ST_LINESTRINGFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_LINESTRINGFROMWKB, 0)

        def ST_NUMGEOMETRIES(self):
            return self.getToken(MySqlBaseParser.ST_NUMGEOMETRIES, 0)

        def ST_NUMINTERIORRING(self):
            return self.getToken(MySqlBaseParser.ST_NUMINTERIORRING, 0)

        def ST_NUMINTERIORRINGS(self):
            return self.getToken(MySqlBaseParser.ST_NUMINTERIORRINGS, 0)

        def ST_NUMPOINTS(self):
            return self.getToken(MySqlBaseParser.ST_NUMPOINTS, 0)

        def ST_OVERLAPS(self):
            return self.getToken(MySqlBaseParser.ST_OVERLAPS, 0)

        def ST_POINTFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_POINTFROMTEXT, 0)

        def ST_POINTFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_POINTFROMWKB, 0)

        def ST_POINTN(self):
            return self.getToken(MySqlBaseParser.ST_POINTN, 0)

        def ST_POLYFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_POLYFROMTEXT, 0)

        def ST_POLYFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_POLYFROMWKB, 0)

        def ST_POLYGONFROMTEXT(self):
            return self.getToken(MySqlBaseParser.ST_POLYGONFROMTEXT, 0)

        def ST_POLYGONFROMWKB(self):
            return self.getToken(MySqlBaseParser.ST_POLYGONFROMWKB, 0)

        def ST_SRID(self):
            return self.getToken(MySqlBaseParser.ST_SRID, 0)

        def ST_STARTPOINT(self):
            return self.getToken(MySqlBaseParser.ST_STARTPOINT, 0)

        def ST_SYMDIFFERENCE(self):
            return self.getToken(MySqlBaseParser.ST_SYMDIFFERENCE, 0)

        def ST_TOUCHES(self):
            return self.getToken(MySqlBaseParser.ST_TOUCHES, 0)

        def ST_UNION(self):
            return self.getToken(MySqlBaseParser.ST_UNION, 0)

        def ST_WITHIN(self):
            return self.getToken(MySqlBaseParser.ST_WITHIN, 0)

        def ST_X(self):
            return self.getToken(MySqlBaseParser.ST_X, 0)

        def ST_Y(self):
            return self.getToken(MySqlBaseParser.ST_Y, 0)

        def SUBDATE(self):
            return self.getToken(MySqlBaseParser.SUBDATE, 0)

        def SUBSTRING_INDEX(self):
            return self.getToken(MySqlBaseParser.SUBSTRING_INDEX, 0)

        def SUBTIME(self):
            return self.getToken(MySqlBaseParser.SUBTIME, 0)

        def SYSTEM_USER(self):
            return self.getToken(MySqlBaseParser.SYSTEM_USER, 0)

        def TAN(self):
            return self.getToken(MySqlBaseParser.TAN, 0)

        def TIME(self):
            return self.getToken(MySqlBaseParser.TIME, 0)

        def TIMEDIFF(self):
            return self.getToken(MySqlBaseParser.TIMEDIFF, 0)

        def TIMESTAMP(self):
            return self.getToken(MySqlBaseParser.TIMESTAMP, 0)

        def TIMESTAMPADD(self):
            return self.getToken(MySqlBaseParser.TIMESTAMPADD, 0)

        def TIMESTAMPDIFF(self):
            return self.getToken(MySqlBaseParser.TIMESTAMPDIFF, 0)

        def TIME_FORMAT(self):
            return self.getToken(MySqlBaseParser.TIME_FORMAT, 0)

        def TIME_TO_SEC(self):
            return self.getToken(MySqlBaseParser.TIME_TO_SEC, 0)

        def TOUCHES(self):
            return self.getToken(MySqlBaseParser.TOUCHES, 0)

        def TO_BASE64(self):
            return self.getToken(MySqlBaseParser.TO_BASE64, 0)

        def TO_DAYS(self):
            return self.getToken(MySqlBaseParser.TO_DAYS, 0)

        def TO_SECONDS(self):
            return self.getToken(MySqlBaseParser.TO_SECONDS, 0)

        def UCASE(self):
            return self.getToken(MySqlBaseParser.UCASE, 0)

        def UNCOMPRESS(self):
            return self.getToken(MySqlBaseParser.UNCOMPRESS, 0)

        def UNCOMPRESSED_LENGTH(self):
            return self.getToken(MySqlBaseParser.UNCOMPRESSED_LENGTH, 0)

        def UNHEX(self):
            return self.getToken(MySqlBaseParser.UNHEX, 0)

        def UNIX_TIMESTAMP(self):
            return self.getToken(MySqlBaseParser.UNIX_TIMESTAMP, 0)

        def UPDATEXML(self):
            return self.getToken(MySqlBaseParser.UPDATEXML, 0)

        def UPPER(self):
            return self.getToken(MySqlBaseParser.UPPER, 0)

        def UUID(self):
            return self.getToken(MySqlBaseParser.UUID, 0)

        def UUID_SHORT(self):
            return self.getToken(MySqlBaseParser.UUID_SHORT, 0)

        def VALIDATE_PASSWORD_STRENGTH(self):
            return self.getToken(MySqlBaseParser.VALIDATE_PASSWORD_STRENGTH, 0)

        def VERSION(self):
            return self.getToken(MySqlBaseParser.VERSION, 0)

        def VISIBLE(self):
            return self.getToken(MySqlBaseParser.VISIBLE, 0)

        def WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS(self):
            return self.getToken(MySqlBaseParser.WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS, 0)

        def WEEK(self):
            return self.getToken(MySqlBaseParser.WEEK, 0)

        def WEEKDAY(self):
            return self.getToken(MySqlBaseParser.WEEKDAY, 0)

        def WEEKOFYEAR(self):
            return self.getToken(MySqlBaseParser.WEEKOFYEAR, 0)

        def WEIGHT_STRING(self):
            return self.getToken(MySqlBaseParser.WEIGHT_STRING, 0)

        def WITHIN(self):
            return self.getToken(MySqlBaseParser.WITHIN, 0)

        def YEAR(self):
            return self.getToken(MySqlBaseParser.YEAR, 0)

        def YEARWEEK(self):
            return self.getToken(MySqlBaseParser.YEARWEEK, 0)

        def Y_FUNCTION(self):
            return self.getToken(MySqlBaseParser.Y_FUNCTION, 0)

        def X_FUNCTION(self):
            return self.getToken(MySqlBaseParser.X_FUNCTION, 0)

        def JSON_ARRAY(self):
            return self.getToken(MySqlBaseParser.JSON_ARRAY, 0)

        def JSON_OBJECT(self):
            return self.getToken(MySqlBaseParser.JSON_OBJECT, 0)

        def JSON_QUOTE(self):
            return self.getToken(MySqlBaseParser.JSON_QUOTE, 0)

        def JSON_CONTAINS(self):
            return self.getToken(MySqlBaseParser.JSON_CONTAINS, 0)

        def JSON_CONTAINS_PATH(self):
            return self.getToken(MySqlBaseParser.JSON_CONTAINS_PATH, 0)

        def JSON_EXTRACT(self):
            return self.getToken(MySqlBaseParser.JSON_EXTRACT, 0)

        def JSON_KEYS(self):
            return self.getToken(MySqlBaseParser.JSON_KEYS, 0)

        def JSON_OVERLAPS(self):
            return self.getToken(MySqlBaseParser.JSON_OVERLAPS, 0)

        def JSON_SEARCH(self):
            return self.getToken(MySqlBaseParser.JSON_SEARCH, 0)

        def JSON_VALUE(self):
            return self.getToken(MySqlBaseParser.JSON_VALUE, 0)

        def JSON_ARRAY_APPEND(self):
            return self.getToken(MySqlBaseParser.JSON_ARRAY_APPEND, 0)

        def JSON_ARRAY_INSERT(self):
            return self.getToken(MySqlBaseParser.JSON_ARRAY_INSERT, 0)

        def JSON_INSERT(self):
            return self.getToken(MySqlBaseParser.JSON_INSERT, 0)

        def JSON_MERGE(self):
            return self.getToken(MySqlBaseParser.JSON_MERGE, 0)

        def JSON_MERGE_PATCH(self):
            return self.getToken(MySqlBaseParser.JSON_MERGE_PATCH, 0)

        def JSON_MERGE_PRESERVE(self):
            return self.getToken(MySqlBaseParser.JSON_MERGE_PRESERVE, 0)

        def JSON_REMOVE(self):
            return self.getToken(MySqlBaseParser.JSON_REMOVE, 0)

        def JSON_REPLACE(self):
            return self.getToken(MySqlBaseParser.JSON_REPLACE, 0)

        def JSON_SET(self):
            return self.getToken(MySqlBaseParser.JSON_SET, 0)

        def JSON_UNQUOTE(self):
            return self.getToken(MySqlBaseParser.JSON_UNQUOTE, 0)

        def JSON_DEPTH(self):
            return self.getToken(MySqlBaseParser.JSON_DEPTH, 0)

        def JSON_LENGTH(self):
            return self.getToken(MySqlBaseParser.JSON_LENGTH, 0)

        def JSON_TYPE(self):
            return self.getToken(MySqlBaseParser.JSON_TYPE, 0)

        def JSON_VALID(self):
            return self.getToken(MySqlBaseParser.JSON_VALID, 0)

        def JSON_TABLE(self):
            return self.getToken(MySqlBaseParser.JSON_TABLE, 0)

        def JSON_SCHEMA_VALID(self):
            return self.getToken(MySqlBaseParser.JSON_SCHEMA_VALID, 0)

        def JSON_SCHEMA_VALIDATION_REPORT(self):
            return self.getToken(MySqlBaseParser.JSON_SCHEMA_VALIDATION_REPORT, 0)

        def JSON_PRETTY(self):
            return self.getToken(MySqlBaseParser.JSON_PRETTY, 0)

        def JSON_STORAGE_FREE(self):
            return self.getToken(MySqlBaseParser.JSON_STORAGE_FREE, 0)

        def JSON_STORAGE_SIZE(self):
            return self.getToken(MySqlBaseParser.JSON_STORAGE_SIZE, 0)

        def JSON_ARRAYAGG(self):
            return self.getToken(MySqlBaseParser.JSON_ARRAYAGG, 0)

        def JSON_OBJECTAGG(self):
            return self.getToken(MySqlBaseParser.JSON_OBJECTAGG, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_functionNameBase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionNameBase" ):
                listener.enterFunctionNameBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionNameBase" ):
                listener.exitFunctionNameBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionNameBase" ):
                return visitor.visitFunctionNameBase(self)
            else:
                return visitor.visitChildren(self)




    def functionNameBase(self):

        localctx = MySqlBaseParser.FunctionNameBaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_functionNameBase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not(_la==MySqlBaseParser.MOD or _la==MySqlBaseParser.DATABASE or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MySqlBaseParser.LEFT - 132)) | (1 << (MySqlBaseParser.RIGHT - 132)) | (1 << (MySqlBaseParser.SCHEMA - 132)))) != 0) or ((((_la - 244)) & ~0x3f) == 0 and ((1 << (_la - 244)) & ((1 << (MySqlBaseParser.DATE - 244)) | (1 << (MySqlBaseParser.TIME - 244)) | (1 << (MySqlBaseParser.TIMESTAMP - 244)) | (1 << (MySqlBaseParser.YEAR - 244)) | (1 << (MySqlBaseParser.JSON_ARRAY - 244)) | (1 << (MySqlBaseParser.JSON_OBJECT - 244)) | (1 << (MySqlBaseParser.JSON_QUOTE - 244)) | (1 << (MySqlBaseParser.JSON_CONTAINS - 244)) | (1 << (MySqlBaseParser.JSON_CONTAINS_PATH - 244)) | (1 << (MySqlBaseParser.JSON_EXTRACT - 244)) | (1 << (MySqlBaseParser.JSON_KEYS - 244)) | (1 << (MySqlBaseParser.JSON_OVERLAPS - 244)) | (1 << (MySqlBaseParser.JSON_SEARCH - 244)) | (1 << (MySqlBaseParser.JSON_VALUE - 244)) | (1 << (MySqlBaseParser.JSON_ARRAY_APPEND - 244)) | (1 << (MySqlBaseParser.JSON_ARRAY_INSERT - 244)) | (1 << (MySqlBaseParser.JSON_INSERT - 244)) | (1 << (MySqlBaseParser.JSON_MERGE - 244)) | (1 << (MySqlBaseParser.JSON_MERGE_PATCH - 244)) | (1 << (MySqlBaseParser.JSON_MERGE_PRESERVE - 244)) | (1 << (MySqlBaseParser.JSON_REMOVE - 244)) | (1 << (MySqlBaseParser.JSON_REPLACE - 244)) | (1 << (MySqlBaseParser.JSON_SET - 244)) | (1 << (MySqlBaseParser.JSON_UNQUOTE - 244)) | (1 << (MySqlBaseParser.JSON_DEPTH - 244)) | (1 << (MySqlBaseParser.JSON_LENGTH - 244)) | (1 << (MySqlBaseParser.JSON_TYPE - 244)) | (1 << (MySqlBaseParser.JSON_VALID - 244)) | (1 << (MySqlBaseParser.JSON_TABLE - 244)) | (1 << (MySqlBaseParser.JSON_SCHEMA_VALID - 244)) | (1 << (MySqlBaseParser.JSON_SCHEMA_VALIDATION_REPORT - 244)) | (1 << (MySqlBaseParser.JSON_PRETTY - 244)) | (1 << (MySqlBaseParser.JSON_STORAGE_FREE - 244)) | (1 << (MySqlBaseParser.JSON_STORAGE_SIZE - 244)))) != 0) or ((((_la - 308)) & ~0x3f) == 0 and ((1 << (_la - 308)) & ((1 << (MySqlBaseParser.JSON_ARRAYAGG - 308)) | (1 << (MySqlBaseParser.JSON_OBJECTAGG - 308)) | (1 << (MySqlBaseParser.COUNT - 308)) | (1 << (MySqlBaseParser.POSITION - 308)))) != 0) or _la==MySqlBaseParser.INVISIBLE or ((((_la - 661)) & ~0x3f) == 0 and ((1 << (_la - 661)) & ((1 << (MySqlBaseParser.VISIBLE - 661)) | (1 << (MySqlBaseParser.QUARTER - 661)) | (1 << (MySqlBaseParser.MONTH - 661)) | (1 << (MySqlBaseParser.DAY - 661)) | (1 << (MySqlBaseParser.HOUR - 661)) | (1 << (MySqlBaseParser.MINUTE - 661)) | (1 << (MySqlBaseParser.WEEK - 661)) | (1 << (MySqlBaseParser.SECOND - 661)) | (1 << (MySqlBaseParser.MICROSECOND - 661)) | (1 << (MySqlBaseParser.SESSION_VARIABLES_ADMIN - 661)))) != 0) or ((((_la - 780)) & ~0x3f) == 0 and ((1 << (_la - 780)) & ((1 << (MySqlBaseParser.GEOMETRYCOLLECTION - 780)) | (1 << (MySqlBaseParser.LINESTRING - 780)) | (1 << (MySqlBaseParser.MULTILINESTRING - 780)) | (1 << (MySqlBaseParser.MULTIPOINT - 780)) | (1 << (MySqlBaseParser.MULTIPOLYGON - 780)) | (1 << (MySqlBaseParser.POINT - 780)) | (1 << (MySqlBaseParser.POLYGON - 780)) | (1 << (MySqlBaseParser.ABS - 780)) | (1 << (MySqlBaseParser.ACOS - 780)) | (1 << (MySqlBaseParser.ADDDATE - 780)) | (1 << (MySqlBaseParser.ADDTIME - 780)) | (1 << (MySqlBaseParser.AES_DECRYPT - 780)) | (1 << (MySqlBaseParser.AES_ENCRYPT - 780)) | (1 << (MySqlBaseParser.AREA - 780)) | (1 << (MySqlBaseParser.ASBINARY - 780)) | (1 << (MySqlBaseParser.ASIN - 780)) | (1 << (MySqlBaseParser.ASTEXT - 780)) | (1 << (MySqlBaseParser.ASWKB - 780)) | (1 << (MySqlBaseParser.ASWKT - 780)) | (1 << (MySqlBaseParser.ASYMMETRIC_DECRYPT - 780)) | (1 << (MySqlBaseParser.ASYMMETRIC_DERIVE - 780)) | (1 << (MySqlBaseParser.ASYMMETRIC_ENCRYPT - 780)) | (1 << (MySqlBaseParser.ASYMMETRIC_SIGN - 780)) | (1 << (MySqlBaseParser.ASYMMETRIC_VERIFY - 780)) | (1 << (MySqlBaseParser.ATAN - 780)) | (1 << (MySqlBaseParser.ATAN2 - 780)) | (1 << (MySqlBaseParser.BENCHMARK - 780)) | (1 << (MySqlBaseParser.BIN - 780)) | (1 << (MySqlBaseParser.BIT_COUNT - 780)) | (1 << (MySqlBaseParser.BIT_LENGTH - 780)) | (1 << (MySqlBaseParser.BUFFER - 780)) | (1 << (MySqlBaseParser.CEIL - 780)) | (1 << (MySqlBaseParser.CEILING - 780)) | (1 << (MySqlBaseParser.CENTROID - 780)) | (1 << (MySqlBaseParser.CHARACTER_LENGTH - 780)) | (1 << (MySqlBaseParser.CHARSET - 780)) | (1 << (MySqlBaseParser.CHAR_LENGTH - 780)) | (1 << (MySqlBaseParser.COERCIBILITY - 780)) | (1 << (MySqlBaseParser.COLLATION - 780)) | (1 << (MySqlBaseParser.COMPRESS - 780)) | (1 << (MySqlBaseParser.CONCAT - 780)) | (1 << (MySqlBaseParser.CONCAT_WS - 780)) | (1 << (MySqlBaseParser.CONNECTION_ID - 780)) | (1 << (MySqlBaseParser.CONV - 780)) | (1 << (MySqlBaseParser.CONVERT_TZ - 780)) | (1 << (MySqlBaseParser.COS - 780)) | (1 << (MySqlBaseParser.COT - 780)) | (1 << (MySqlBaseParser.CRC32 - 780)) | (1 << (MySqlBaseParser.CREATE_ASYMMETRIC_PRIV_KEY - 780)) | (1 << (MySqlBaseParser.CREATE_ASYMMETRIC_PUB_KEY - 780)) | (1 << (MySqlBaseParser.CREATE_DH_PARAMETERS - 780)) | (1 << (MySqlBaseParser.CREATE_DIGEST - 780)) | (1 << (MySqlBaseParser.CROSSES - 780)) | (1 << (MySqlBaseParser.DATEDIFF - 780)) | (1 << (MySqlBaseParser.DATE_FORMAT - 780)) | (1 << (MySqlBaseParser.DAYNAME - 780)) | (1 << (MySqlBaseParser.DAYOFMONTH - 780)) | (1 << (MySqlBaseParser.DAYOFWEEK - 780)) | (1 << (MySqlBaseParser.DAYOFYEAR - 780)) | (1 << (MySqlBaseParser.DECODE - 780)) | (1 << (MySqlBaseParser.DEGREES - 780)))) != 0) or ((((_la - 844)) & ~0x3f) == 0 and ((1 << (_la - 844)) & ((1 << (MySqlBaseParser.DES_DECRYPT - 844)) | (1 << (MySqlBaseParser.DES_ENCRYPT - 844)) | (1 << (MySqlBaseParser.DIMENSION - 844)) | (1 << (MySqlBaseParser.DISJOINT - 844)) | (1 << (MySqlBaseParser.ELT - 844)) | (1 << (MySqlBaseParser.ENCODE - 844)) | (1 << (MySqlBaseParser.ENCRYPT - 844)) | (1 << (MySqlBaseParser.ENDPOINT - 844)) | (1 << (MySqlBaseParser.ENVELOPE - 844)) | (1 << (MySqlBaseParser.EQUALS - 844)) | (1 << (MySqlBaseParser.EXP - 844)) | (1 << (MySqlBaseParser.EXPORT_SET - 844)) | (1 << (MySqlBaseParser.EXTERIORRING - 844)) | (1 << (MySqlBaseParser.EXTRACTVALUE - 844)) | (1 << (MySqlBaseParser.FIELD - 844)) | (1 << (MySqlBaseParser.FIND_IN_SET - 844)) | (1 << (MySqlBaseParser.FLOOR - 844)) | (1 << (MySqlBaseParser.FORMAT - 844)) | (1 << (MySqlBaseParser.FOUND_ROWS - 844)) | (1 << (MySqlBaseParser.FROM_BASE64 - 844)) | (1 << (MySqlBaseParser.FROM_DAYS - 844)) | (1 << (MySqlBaseParser.FROM_UNIXTIME - 844)) | (1 << (MySqlBaseParser.GEOMCOLLFROMTEXT - 844)) | (1 << (MySqlBaseParser.GEOMCOLLFROMWKB - 844)) | (1 << (MySqlBaseParser.GEOMETRYCOLLECTIONFROMTEXT - 844)) | (1 << (MySqlBaseParser.GEOMETRYCOLLECTIONFROMWKB - 844)) | (1 << (MySqlBaseParser.GEOMETRYFROMTEXT - 844)) | (1 << (MySqlBaseParser.GEOMETRYFROMWKB - 844)) | (1 << (MySqlBaseParser.GEOMETRYN - 844)) | (1 << (MySqlBaseParser.GEOMETRYTYPE - 844)) | (1 << (MySqlBaseParser.GEOMFROMTEXT - 844)) | (1 << (MySqlBaseParser.GEOMFROMWKB - 844)) | (1 << (MySqlBaseParser.GET_FORMAT - 844)) | (1 << (MySqlBaseParser.GET_LOCK - 844)) | (1 << (MySqlBaseParser.GLENGTH - 844)) | (1 << (MySqlBaseParser.GREATEST - 844)) | (1 << (MySqlBaseParser.GTID_SUBSET - 844)) | (1 << (MySqlBaseParser.GTID_SUBTRACT - 844)) | (1 << (MySqlBaseParser.HEX - 844)) | (1 << (MySqlBaseParser.IFNULL - 844)) | (1 << (MySqlBaseParser.INET6_ATON - 844)) | (1 << (MySqlBaseParser.INET6_NTOA - 844)) | (1 << (MySqlBaseParser.INET_ATON - 844)) | (1 << (MySqlBaseParser.INET_NTOA - 844)) | (1 << (MySqlBaseParser.INSTR - 844)) | (1 << (MySqlBaseParser.INTERIORRINGN - 844)) | (1 << (MySqlBaseParser.INTERSECTS - 844)) | (1 << (MySqlBaseParser.ISCLOSED - 844)) | (1 << (MySqlBaseParser.ISEMPTY - 844)) | (1 << (MySqlBaseParser.ISNULL - 844)) | (1 << (MySqlBaseParser.ISSIMPLE - 844)) | (1 << (MySqlBaseParser.IS_FREE_LOCK - 844)) | (1 << (MySqlBaseParser.IS_IPV4 - 844)) | (1 << (MySqlBaseParser.IS_IPV4_COMPAT - 844)) | (1 << (MySqlBaseParser.IS_IPV4_MAPPED - 844)) | (1 << (MySqlBaseParser.IS_IPV6 - 844)) | (1 << (MySqlBaseParser.IS_USED_LOCK - 844)) | (1 << (MySqlBaseParser.LAST_INSERT_ID - 844)) | (1 << (MySqlBaseParser.LCASE - 844)) | (1 << (MySqlBaseParser.LEAST - 844)) | (1 << (MySqlBaseParser.LENGTH - 844)) | (1 << (MySqlBaseParser.LINEFROMTEXT - 844)) | (1 << (MySqlBaseParser.LINEFROMWKB - 844)) | (1 << (MySqlBaseParser.LINESTRINGFROMTEXT - 844)))) != 0) or ((((_la - 908)) & ~0x3f) == 0 and ((1 << (_la - 908)) & ((1 << (MySqlBaseParser.LINESTRINGFROMWKB - 908)) | (1 << (MySqlBaseParser.LN - 908)) | (1 << (MySqlBaseParser.LOAD_FILE - 908)) | (1 << (MySqlBaseParser.LOCATE - 908)) | (1 << (MySqlBaseParser.LOG - 908)) | (1 << (MySqlBaseParser.LOG10 - 908)) | (1 << (MySqlBaseParser.LOG2 - 908)) | (1 << (MySqlBaseParser.LOWER - 908)) | (1 << (MySqlBaseParser.LPAD - 908)) | (1 << (MySqlBaseParser.LTRIM - 908)) | (1 << (MySqlBaseParser.MAKEDATE - 908)) | (1 << (MySqlBaseParser.MAKETIME - 908)) | (1 << (MySqlBaseParser.MAKE_SET - 908)) | (1 << (MySqlBaseParser.MASTER_POS_WAIT - 908)) | (1 << (MySqlBaseParser.MBRCONTAINS - 908)) | (1 << (MySqlBaseParser.MBRDISJOINT - 908)) | (1 << (MySqlBaseParser.MBREQUAL - 908)) | (1 << (MySqlBaseParser.MBRINTERSECTS - 908)) | (1 << (MySqlBaseParser.MBROVERLAPS - 908)) | (1 << (MySqlBaseParser.MBRTOUCHES - 908)) | (1 << (MySqlBaseParser.MBRWITHIN - 908)) | (1 << (MySqlBaseParser.MD5 - 908)) | (1 << (MySqlBaseParser.MLINEFROMTEXT - 908)) | (1 << (MySqlBaseParser.MLINEFROMWKB - 908)) | (1 << (MySqlBaseParser.MONTHNAME - 908)) | (1 << (MySqlBaseParser.MPOINTFROMTEXT - 908)) | (1 << (MySqlBaseParser.MPOINTFROMWKB - 908)) | (1 << (MySqlBaseParser.MPOLYFROMTEXT - 908)) | (1 << (MySqlBaseParser.MPOLYFROMWKB - 908)) | (1 << (MySqlBaseParser.MULTILINESTRINGFROMTEXT - 908)) | (1 << (MySqlBaseParser.MULTILINESTRINGFROMWKB - 908)) | (1 << (MySqlBaseParser.MULTIPOINTFROMTEXT - 908)) | (1 << (MySqlBaseParser.MULTIPOINTFROMWKB - 908)) | (1 << (MySqlBaseParser.MULTIPOLYGONFROMTEXT - 908)) | (1 << (MySqlBaseParser.MULTIPOLYGONFROMWKB - 908)) | (1 << (MySqlBaseParser.NAME_CONST - 908)) | (1 << (MySqlBaseParser.NULLIF - 908)) | (1 << (MySqlBaseParser.NUMGEOMETRIES - 908)) | (1 << (MySqlBaseParser.NUMINTERIORRINGS - 908)) | (1 << (MySqlBaseParser.NUMPOINTS - 908)) | (1 << (MySqlBaseParser.OCT - 908)) | (1 << (MySqlBaseParser.OCTET_LENGTH - 908)) | (1 << (MySqlBaseParser.ORD - 908)) | (1 << (MySqlBaseParser.OVERLAPS - 908)) | (1 << (MySqlBaseParser.PERIOD_ADD - 908)) | (1 << (MySqlBaseParser.PERIOD_DIFF - 908)) | (1 << (MySqlBaseParser.PI - 908)) | (1 << (MySqlBaseParser.POINTFROMTEXT - 908)) | (1 << (MySqlBaseParser.POINTFROMWKB - 908)) | (1 << (MySqlBaseParser.POINTN - 908)) | (1 << (MySqlBaseParser.POLYFROMTEXT - 908)) | (1 << (MySqlBaseParser.POLYFROMWKB - 908)) | (1 << (MySqlBaseParser.POLYGONFROMTEXT - 908)) | (1 << (MySqlBaseParser.POLYGONFROMWKB - 908)) | (1 << (MySqlBaseParser.POW - 908)) | (1 << (MySqlBaseParser.POWER - 908)) | (1 << (MySqlBaseParser.QUOTE - 908)) | (1 << (MySqlBaseParser.RADIANS - 908)) | (1 << (MySqlBaseParser.RAND - 908)) | (1 << (MySqlBaseParser.RANDOM_BYTES - 908)) | (1 << (MySqlBaseParser.RELEASE_LOCK - 908)) | (1 << (MySqlBaseParser.REVERSE - 908)) | (1 << (MySqlBaseParser.ROUND - 908)) | (1 << (MySqlBaseParser.ROW_COUNT - 908)))) != 0) or ((((_la - 972)) & ~0x3f) == 0 and ((1 << (_la - 972)) & ((1 << (MySqlBaseParser.RPAD - 972)) | (1 << (MySqlBaseParser.RTRIM - 972)) | (1 << (MySqlBaseParser.SEC_TO_TIME - 972)) | (1 << (MySqlBaseParser.SESSION_USER - 972)) | (1 << (MySqlBaseParser.SHA - 972)) | (1 << (MySqlBaseParser.SHA1 - 972)) | (1 << (MySqlBaseParser.SHA2 - 972)) | (1 << (MySqlBaseParser.SIGN - 972)) | (1 << (MySqlBaseParser.SIN - 972)) | (1 << (MySqlBaseParser.SLEEP - 972)) | (1 << (MySqlBaseParser.SOUNDEX - 972)) | (1 << (MySqlBaseParser.SQL_THREAD_WAIT_AFTER_GTIDS - 972)) | (1 << (MySqlBaseParser.SQRT - 972)) | (1 << (MySqlBaseParser.SRID - 972)) | (1 << (MySqlBaseParser.STARTPOINT - 972)) | (1 << (MySqlBaseParser.STRCMP - 972)) | (1 << (MySqlBaseParser.STR_TO_DATE - 972)) | (1 << (MySqlBaseParser.ST_AREA - 972)) | (1 << (MySqlBaseParser.ST_ASBINARY - 972)) | (1 << (MySqlBaseParser.ST_ASTEXT - 972)) | (1 << (MySqlBaseParser.ST_ASWKB - 972)) | (1 << (MySqlBaseParser.ST_ASWKT - 972)) | (1 << (MySqlBaseParser.ST_BUFFER - 972)) | (1 << (MySqlBaseParser.ST_CENTROID - 972)) | (1 << (MySqlBaseParser.ST_CONTAINS - 972)) | (1 << (MySqlBaseParser.ST_CROSSES - 972)) | (1 << (MySqlBaseParser.ST_DIFFERENCE - 972)) | (1 << (MySqlBaseParser.ST_DIMENSION - 972)) | (1 << (MySqlBaseParser.ST_DISJOINT - 972)) | (1 << (MySqlBaseParser.ST_DISTANCE - 972)) | (1 << (MySqlBaseParser.ST_ENDPOINT - 972)) | (1 << (MySqlBaseParser.ST_ENVELOPE - 972)) | (1 << (MySqlBaseParser.ST_EQUALS - 972)) | (1 << (MySqlBaseParser.ST_EXTERIORRING - 972)) | (1 << (MySqlBaseParser.ST_GEOMCOLLFROMTEXT - 972)) | (1 << (MySqlBaseParser.ST_GEOMCOLLFROMTXT - 972)) | (1 << (MySqlBaseParser.ST_GEOMCOLLFROMWKB - 972)) | (1 << (MySqlBaseParser.ST_GEOMETRYCOLLECTIONFROMTEXT - 972)) | (1 << (MySqlBaseParser.ST_GEOMETRYCOLLECTIONFROMWKB - 972)) | (1 << (MySqlBaseParser.ST_GEOMETRYFROMTEXT - 972)) | (1 << (MySqlBaseParser.ST_GEOMETRYFROMWKB - 972)) | (1 << (MySqlBaseParser.ST_GEOMETRYN - 972)) | (1 << (MySqlBaseParser.ST_GEOMETRYTYPE - 972)) | (1 << (MySqlBaseParser.ST_GEOMFROMTEXT - 972)) | (1 << (MySqlBaseParser.ST_GEOMFROMWKB - 972)) | (1 << (MySqlBaseParser.ST_INTERIORRINGN - 972)) | (1 << (MySqlBaseParser.ST_INTERSECTION - 972)) | (1 << (MySqlBaseParser.ST_INTERSECTS - 972)) | (1 << (MySqlBaseParser.ST_ISCLOSED - 972)) | (1 << (MySqlBaseParser.ST_ISEMPTY - 972)) | (1 << (MySqlBaseParser.ST_ISSIMPLE - 972)) | (1 << (MySqlBaseParser.ST_LINEFROMTEXT - 972)) | (1 << (MySqlBaseParser.ST_LINEFROMWKB - 972)) | (1 << (MySqlBaseParser.ST_LINESTRINGFROMTEXT - 972)) | (1 << (MySqlBaseParser.ST_LINESTRINGFROMWKB - 972)) | (1 << (MySqlBaseParser.ST_NUMGEOMETRIES - 972)) | (1 << (MySqlBaseParser.ST_NUMINTERIORRING - 972)) | (1 << (MySqlBaseParser.ST_NUMINTERIORRINGS - 972)) | (1 << (MySqlBaseParser.ST_NUMPOINTS - 972)) | (1 << (MySqlBaseParser.ST_OVERLAPS - 972)) | (1 << (MySqlBaseParser.ST_POINTFROMTEXT - 972)) | (1 << (MySqlBaseParser.ST_POINTFROMWKB - 972)) | (1 << (MySqlBaseParser.ST_POINTN - 972)))) != 0) or ((((_la - 1036)) & ~0x3f) == 0 and ((1 << (_la - 1036)) & ((1 << (MySqlBaseParser.ST_POLYFROMTEXT - 1036)) | (1 << (MySqlBaseParser.ST_POLYFROMWKB - 1036)) | (1 << (MySqlBaseParser.ST_POLYGONFROMTEXT - 1036)) | (1 << (MySqlBaseParser.ST_POLYGONFROMWKB - 1036)) | (1 << (MySqlBaseParser.ST_SRID - 1036)) | (1 << (MySqlBaseParser.ST_STARTPOINT - 1036)) | (1 << (MySqlBaseParser.ST_SYMDIFFERENCE - 1036)) | (1 << (MySqlBaseParser.ST_TOUCHES - 1036)) | (1 << (MySqlBaseParser.ST_UNION - 1036)) | (1 << (MySqlBaseParser.ST_WITHIN - 1036)) | (1 << (MySqlBaseParser.ST_X - 1036)) | (1 << (MySqlBaseParser.ST_Y - 1036)) | (1 << (MySqlBaseParser.SUBDATE - 1036)) | (1 << (MySqlBaseParser.SUBSTRING_INDEX - 1036)) | (1 << (MySqlBaseParser.SUBTIME - 1036)) | (1 << (MySqlBaseParser.SYSTEM_USER - 1036)) | (1 << (MySqlBaseParser.TAN - 1036)) | (1 << (MySqlBaseParser.TIMEDIFF - 1036)) | (1 << (MySqlBaseParser.TIMESTAMPADD - 1036)) | (1 << (MySqlBaseParser.TIMESTAMPDIFF - 1036)) | (1 << (MySqlBaseParser.TIME_FORMAT - 1036)) | (1 << (MySqlBaseParser.TIME_TO_SEC - 1036)) | (1 << (MySqlBaseParser.TOUCHES - 1036)) | (1 << (MySqlBaseParser.TO_BASE64 - 1036)) | (1 << (MySqlBaseParser.TO_DAYS - 1036)) | (1 << (MySqlBaseParser.TO_SECONDS - 1036)) | (1 << (MySqlBaseParser.UCASE - 1036)) | (1 << (MySqlBaseParser.UNCOMPRESS - 1036)) | (1 << (MySqlBaseParser.UNCOMPRESSED_LENGTH - 1036)) | (1 << (MySqlBaseParser.UNHEX - 1036)) | (1 << (MySqlBaseParser.UNIX_TIMESTAMP - 1036)) | (1 << (MySqlBaseParser.UPDATEXML - 1036)) | (1 << (MySqlBaseParser.UPPER - 1036)) | (1 << (MySqlBaseParser.UUID - 1036)) | (1 << (MySqlBaseParser.UUID_SHORT - 1036)) | (1 << (MySqlBaseParser.VALIDATE_PASSWORD_STRENGTH - 1036)) | (1 << (MySqlBaseParser.VERSION - 1036)) | (1 << (MySqlBaseParser.WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS - 1036)) | (1 << (MySqlBaseParser.WEEKDAY - 1036)) | (1 << (MySqlBaseParser.WEEKOFYEAR - 1036)) | (1 << (MySqlBaseParser.WEIGHT_STRING - 1036)) | (1 << (MySqlBaseParser.WITHIN - 1036)) | (1 << (MySqlBaseParser.YEARWEEK - 1036)) | (1 << (MySqlBaseParser.Y_FUNCTION - 1036)) | (1 << (MySqlBaseParser.X_FUNCTION - 1036)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SYMBOL(self):
            return self.getToken(MySqlBaseParser.EQUAL_SYMBOL, 0)

        def GREATER_SYMBOL(self):
            return self.getToken(MySqlBaseParser.GREATER_SYMBOL, 0)

        def LESS_SYMBOL(self):
            return self.getToken(MySqlBaseParser.LESS_SYMBOL, 0)

        def EXCLAMATION_SYMBOL(self):
            return self.getToken(MySqlBaseParser.EXCLAMATION_SYMBOL, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = MySqlBaseParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_comparisonOperator)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(MySqlBaseParser.EQUAL_SYMBOL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(MySqlBaseParser.GREATER_SYMBOL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 424
                self.match(MySqlBaseParser.LESS_SYMBOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 425
                self.match(MySqlBaseParser.LESS_SYMBOL)
                self.state = 426
                self.match(MySqlBaseParser.EQUAL_SYMBOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 427
                self.match(MySqlBaseParser.GREATER_SYMBOL)
                self.state = 428
                self.match(MySqlBaseParser.EQUAL_SYMBOL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 429
                self.match(MySqlBaseParser.LESS_SYMBOL)
                self.state = 430
                self.match(MySqlBaseParser.GREATER_SYMBOL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 431
                self.match(MySqlBaseParser.EXCLAMATION_SYMBOL)
                self.state = 432
                self.match(MySqlBaseParser.EQUAL_SYMBOL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 433
                self.match(MySqlBaseParser.LESS_SYMBOL)
                self.state = 434
                self.match(MySqlBaseParser.EQUAL_SYMBOL)
                self.state = 435
                self.match(MySqlBaseParser.GREATER_SYMBOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(MySqlBaseParser.AND, 0)

        def BIT_AND_OP(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.BIT_AND_OP)
            else:
                return self.getToken(MySqlBaseParser.BIT_AND_OP, i)

        def XOR(self):
            return self.getToken(MySqlBaseParser.XOR, 0)

        def OR(self):
            return self.getToken(MySqlBaseParser.OR, 0)

        def BIT_OR_OP(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.BIT_OR_OP)
            else:
                return self.getToken(MySqlBaseParser.BIT_OR_OP, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_logicalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOperator" ):
                listener.enterLogicalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOperator" ):
                listener.exitLogicalOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOperator" ):
                return visitor.visitLogicalOperator(self)
            else:
                return visitor.visitChildren(self)




    def logicalOperator(self):

        localctx = MySqlBaseParser.LogicalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_logicalOperator)
        try:
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.AND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(MySqlBaseParser.AND)
                pass
            elif token in [MySqlBaseParser.BIT_AND_OP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(MySqlBaseParser.BIT_AND_OP)
                self.state = 440
                self.match(MySqlBaseParser.BIT_AND_OP)
                pass
            elif token in [MySqlBaseParser.XOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.match(MySqlBaseParser.XOR)
                pass
            elif token in [MySqlBaseParser.OR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 442
                self.match(MySqlBaseParser.OR)
                pass
            elif token in [MySqlBaseParser.BIT_OR_OP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 443
                self.match(MySqlBaseParser.BIT_OR_OP)
                self.state = 444
                self.match(MySqlBaseParser.BIT_OR_OP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordsCanBeIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCOUNT(self):
            return self.getToken(MySqlBaseParser.ACCOUNT, 0)

        def ACTION(self):
            return self.getToken(MySqlBaseParser.ACTION, 0)

        def AFTER(self):
            return self.getToken(MySqlBaseParser.AFTER, 0)

        def AGGREGATE(self):
            return self.getToken(MySqlBaseParser.AGGREGATE, 0)

        def ALGORITHM(self):
            return self.getToken(MySqlBaseParser.ALGORITHM, 0)

        def ANY(self):
            return self.getToken(MySqlBaseParser.ANY, 0)

        def AT(self):
            return self.getToken(MySqlBaseParser.AT, 0)

        def AUDIT_ADMIN(self):
            return self.getToken(MySqlBaseParser.AUDIT_ADMIN, 0)

        def AUTHORS(self):
            return self.getToken(MySqlBaseParser.AUTHORS, 0)

        def AUTOCOMMIT(self):
            return self.getToken(MySqlBaseParser.AUTOCOMMIT, 0)

        def AUTOEXTEND_SIZE(self):
            return self.getToken(MySqlBaseParser.AUTOEXTEND_SIZE, 0)

        def AUTO_INCREMENT(self):
            return self.getToken(MySqlBaseParser.AUTO_INCREMENT, 0)

        def AVG(self):
            return self.getToken(MySqlBaseParser.AVG, 0)

        def AVG_ROW_LENGTH(self):
            return self.getToken(MySqlBaseParser.AVG_ROW_LENGTH, 0)

        def BACKUP_ADMIN(self):
            return self.getToken(MySqlBaseParser.BACKUP_ADMIN, 0)

        def BEGIN(self):
            return self.getToken(MySqlBaseParser.BEGIN, 0)

        def BINLOG(self):
            return self.getToken(MySqlBaseParser.BINLOG, 0)

        def BINLOG_ADMIN(self):
            return self.getToken(MySqlBaseParser.BINLOG_ADMIN, 0)

        def BINLOG_ENCRYPTION_ADMIN(self):
            return self.getToken(MySqlBaseParser.BINLOG_ENCRYPTION_ADMIN, 0)

        def BIT(self):
            return self.getToken(MySqlBaseParser.BIT, 0)

        def BIT_AND(self):
            return self.getToken(MySqlBaseParser.BIT_AND, 0)

        def BIT_OR(self):
            return self.getToken(MySqlBaseParser.BIT_OR, 0)

        def BIT_XOR(self):
            return self.getToken(MySqlBaseParser.BIT_XOR, 0)

        def BLOCK(self):
            return self.getToken(MySqlBaseParser.BLOCK, 0)

        def BOOL(self):
            return self.getToken(MySqlBaseParser.BOOL, 0)

        def BOOLEAN(self):
            return self.getToken(MySqlBaseParser.BOOLEAN, 0)

        def BTREE(self):
            return self.getToken(MySqlBaseParser.BTREE, 0)

        def CACHE(self):
            return self.getToken(MySqlBaseParser.CACHE, 0)

        def CASCADED(self):
            return self.getToken(MySqlBaseParser.CASCADED, 0)

        def CHAIN(self):
            return self.getToken(MySqlBaseParser.CHAIN, 0)

        def CHANGED(self):
            return self.getToken(MySqlBaseParser.CHANGED, 0)

        def CHANNEL(self):
            return self.getToken(MySqlBaseParser.CHANNEL, 0)

        def CHECKSUM(self):
            return self.getToken(MySqlBaseParser.CHECKSUM, 0)

        def PAGE_CHECKSUM(self):
            return self.getToken(MySqlBaseParser.PAGE_CHECKSUM, 0)

        def CATALOG_NAME(self):
            return self.getToken(MySqlBaseParser.CATALOG_NAME, 0)

        def CIPHER(self):
            return self.getToken(MySqlBaseParser.CIPHER, 0)

        def CLASS_ORIGIN(self):
            return self.getToken(MySqlBaseParser.CLASS_ORIGIN, 0)

        def CLIENT(self):
            return self.getToken(MySqlBaseParser.CLIENT, 0)

        def CLONE_ADMIN(self):
            return self.getToken(MySqlBaseParser.CLONE_ADMIN, 0)

        def CLOSE(self):
            return self.getToken(MySqlBaseParser.CLOSE, 0)

        def COALESCE(self):
            return self.getToken(MySqlBaseParser.COALESCE, 0)

        def CODE(self):
            return self.getToken(MySqlBaseParser.CODE, 0)

        def COLUMNS(self):
            return self.getToken(MySqlBaseParser.COLUMNS, 0)

        def COLUMN_FORMAT(self):
            return self.getToken(MySqlBaseParser.COLUMN_FORMAT, 0)

        def COLUMN_NAME(self):
            return self.getToken(MySqlBaseParser.COLUMN_NAME, 0)

        def COMMENT(self):
            return self.getToken(MySqlBaseParser.COMMENT, 0)

        def COMMIT(self):
            return self.getToken(MySqlBaseParser.COMMIT, 0)

        def COMPACT(self):
            return self.getToken(MySqlBaseParser.COMPACT, 0)

        def COMPLETION(self):
            return self.getToken(MySqlBaseParser.COMPLETION, 0)

        def COMPRESSED(self):
            return self.getToken(MySqlBaseParser.COMPRESSED, 0)

        def COMPRESSION(self):
            return self.getToken(MySqlBaseParser.COMPRESSION, 0)

        def CONCURRENT(self):
            return self.getToken(MySqlBaseParser.CONCURRENT, 0)

        def CONNECT(self):
            return self.getToken(MySqlBaseParser.CONNECT, 0)

        def CONNECTION(self):
            return self.getToken(MySqlBaseParser.CONNECTION, 0)

        def CONNECTION_ADMIN(self):
            return self.getToken(MySqlBaseParser.CONNECTION_ADMIN, 0)

        def CONSISTENT(self):
            return self.getToken(MySqlBaseParser.CONSISTENT, 0)

        def CONSTRAINT_CATALOG(self):
            return self.getToken(MySqlBaseParser.CONSTRAINT_CATALOG, 0)

        def CONSTRAINT_NAME(self):
            return self.getToken(MySqlBaseParser.CONSTRAINT_NAME, 0)

        def CONSTRAINT_SCHEMA(self):
            return self.getToken(MySqlBaseParser.CONSTRAINT_SCHEMA, 0)

        def CONTAINS(self):
            return self.getToken(MySqlBaseParser.CONTAINS, 0)

        def CONTEXT(self):
            return self.getToken(MySqlBaseParser.CONTEXT, 0)

        def CONTRIBUTORS(self):
            return self.getToken(MySqlBaseParser.CONTRIBUTORS, 0)

        def COPY(self):
            return self.getToken(MySqlBaseParser.COPY, 0)

        def COUNT(self):
            return self.getToken(MySqlBaseParser.COUNT, 0)

        def CPU(self):
            return self.getToken(MySqlBaseParser.CPU, 0)

        def CURRENT(self):
            return self.getToken(MySqlBaseParser.CURRENT, 0)

        def CURSOR_NAME(self):
            return self.getToken(MySqlBaseParser.CURSOR_NAME, 0)

        def DATA(self):
            return self.getToken(MySqlBaseParser.DATA, 0)

        def DATAFILE(self):
            return self.getToken(MySqlBaseParser.DATAFILE, 0)

        def DEALLOCATE(self):
            return self.getToken(MySqlBaseParser.DEALLOCATE, 0)

        def DEFAULT_AUTH(self):
            return self.getToken(MySqlBaseParser.DEFAULT_AUTH, 0)

        def DEFINER(self):
            return self.getToken(MySqlBaseParser.DEFINER, 0)

        def DELAY_KEY_WRITE(self):
            return self.getToken(MySqlBaseParser.DELAY_KEY_WRITE, 0)

        def DES_KEY_FILE(self):
            return self.getToken(MySqlBaseParser.DES_KEY_FILE, 0)

        def DIAGNOSTICS(self):
            return self.getToken(MySqlBaseParser.DIAGNOSTICS, 0)

        def DIRECTORY(self):
            return self.getToken(MySqlBaseParser.DIRECTORY, 0)

        def DISABLE(self):
            return self.getToken(MySqlBaseParser.DISABLE, 0)

        def DISCARD(self):
            return self.getToken(MySqlBaseParser.DISCARD, 0)

        def DISK(self):
            return self.getToken(MySqlBaseParser.DISK, 0)

        def DO(self):
            return self.getToken(MySqlBaseParser.DO, 0)

        def DUMPFILE(self):
            return self.getToken(MySqlBaseParser.DUMPFILE, 0)

        def DUPLICATE(self):
            return self.getToken(MySqlBaseParser.DUPLICATE, 0)

        def DYNAMIC(self):
            return self.getToken(MySqlBaseParser.DYNAMIC, 0)

        def ENABLE(self):
            return self.getToken(MySqlBaseParser.ENABLE, 0)

        def ENCRYPTION(self):
            return self.getToken(MySqlBaseParser.ENCRYPTION, 0)

        def ENCRYPTION_KEY_ADMIN(self):
            return self.getToken(MySqlBaseParser.ENCRYPTION_KEY_ADMIN, 0)

        def END(self):
            return self.getToken(MySqlBaseParser.END, 0)

        def ENDS(self):
            return self.getToken(MySqlBaseParser.ENDS, 0)

        def ENGINE(self):
            return self.getToken(MySqlBaseParser.ENGINE, 0)

        def ENGINES(self):
            return self.getToken(MySqlBaseParser.ENGINES, 0)

        def ERROR(self):
            return self.getToken(MySqlBaseParser.ERROR, 0)

        def ERRORS(self):
            return self.getToken(MySqlBaseParser.ERRORS, 0)

        def ESCAPE(self):
            return self.getToken(MySqlBaseParser.ESCAPE, 0)

        def EVEN(self):
            return self.getToken(MySqlBaseParser.EVEN, 0)

        def EVENT(self):
            return self.getToken(MySqlBaseParser.EVENT, 0)

        def EVENTS(self):
            return self.getToken(MySqlBaseParser.EVENTS, 0)

        def EVERY(self):
            return self.getToken(MySqlBaseParser.EVERY, 0)

        def EXCHANGE(self):
            return self.getToken(MySqlBaseParser.EXCHANGE, 0)

        def EXCLUSIVE(self):
            return self.getToken(MySqlBaseParser.EXCLUSIVE, 0)

        def EXPIRE(self):
            return self.getToken(MySqlBaseParser.EXPIRE, 0)

        def EXPORT(self):
            return self.getToken(MySqlBaseParser.EXPORT, 0)

        def EXTENDED(self):
            return self.getToken(MySqlBaseParser.EXTENDED, 0)

        def EXTENT_SIZE(self):
            return self.getToken(MySqlBaseParser.EXTENT_SIZE, 0)

        def FAST(self):
            return self.getToken(MySqlBaseParser.FAST, 0)

        def FAULTS(self):
            return self.getToken(MySqlBaseParser.FAULTS, 0)

        def FIELDS(self):
            return self.getToken(MySqlBaseParser.FIELDS, 0)

        def FILE_BLOCK_SIZE(self):
            return self.getToken(MySqlBaseParser.FILE_BLOCK_SIZE, 0)

        def FILTER(self):
            return self.getToken(MySqlBaseParser.FILTER, 0)

        def FIREWALL_ADMIN(self):
            return self.getToken(MySqlBaseParser.FIREWALL_ADMIN, 0)

        def FIREWALL_USER(self):
            return self.getToken(MySqlBaseParser.FIREWALL_USER, 0)

        def FIRST(self):
            return self.getToken(MySqlBaseParser.FIRST, 0)

        def FIXED(self):
            return self.getToken(MySqlBaseParser.FIXED, 0)

        def FLUSH(self):
            return self.getToken(MySqlBaseParser.FLUSH, 0)

        def FOLLOWS(self):
            return self.getToken(MySqlBaseParser.FOLLOWS, 0)

        def FOUND(self):
            return self.getToken(MySqlBaseParser.FOUND, 0)

        def FULL(self):
            return self.getToken(MySqlBaseParser.FULL, 0)

        def FUNCTION(self):
            return self.getToken(MySqlBaseParser.FUNCTION, 0)

        def GENERAL(self):
            return self.getToken(MySqlBaseParser.GENERAL, 0)

        def GLOBAL(self):
            return self.getToken(MySqlBaseParser.GLOBAL, 0)

        def GRANTS(self):
            return self.getToken(MySqlBaseParser.GRANTS, 0)

        def GROUP(self):
            return self.getToken(MySqlBaseParser.GROUP, 0)

        def GROUP_CONCAT(self):
            return self.getToken(MySqlBaseParser.GROUP_CONCAT, 0)

        def GROUP_REPLICATION(self):
            return self.getToken(MySqlBaseParser.GROUP_REPLICATION, 0)

        def GROUP_REPLICATION_ADMIN(self):
            return self.getToken(MySqlBaseParser.GROUP_REPLICATION_ADMIN, 0)

        def HANDLER(self):
            return self.getToken(MySqlBaseParser.HANDLER, 0)

        def HASH(self):
            return self.getToken(MySqlBaseParser.HASH, 0)

        def HELP(self):
            return self.getToken(MySqlBaseParser.HELP, 0)

        def HOST(self):
            return self.getToken(MySqlBaseParser.HOST, 0)

        def HOSTS(self):
            return self.getToken(MySqlBaseParser.HOSTS, 0)

        def IDENTIFIED(self):
            return self.getToken(MySqlBaseParser.IDENTIFIED, 0)

        def IGNORE_SERVER_IDS(self):
            return self.getToken(MySqlBaseParser.IGNORE_SERVER_IDS, 0)

        def IMPORT(self):
            return self.getToken(MySqlBaseParser.IMPORT, 0)

        def INDEXES(self):
            return self.getToken(MySqlBaseParser.INDEXES, 0)

        def INITIAL_SIZE(self):
            return self.getToken(MySqlBaseParser.INITIAL_SIZE, 0)

        def INNODB_REDO_LOG_ARCHIVE(self):
            return self.getToken(MySqlBaseParser.INNODB_REDO_LOG_ARCHIVE, 0)

        def INPLACE(self):
            return self.getToken(MySqlBaseParser.INPLACE, 0)

        def INSERT_METHOD(self):
            return self.getToken(MySqlBaseParser.INSERT_METHOD, 0)

        def INSTALL(self):
            return self.getToken(MySqlBaseParser.INSTALL, 0)

        def INSTANCE(self):
            return self.getToken(MySqlBaseParser.INSTANCE, 0)

        def INTERNAL(self):
            return self.getToken(MySqlBaseParser.INTERNAL, 0)

        def INVOKER(self):
            return self.getToken(MySqlBaseParser.INVOKER, 0)

        def IO(self):
            return self.getToken(MySqlBaseParser.IO, 0)

        def IO_THREAD(self):
            return self.getToken(MySqlBaseParser.IO_THREAD, 0)

        def IPC(self):
            return self.getToken(MySqlBaseParser.IPC, 0)

        def ISOLATION(self):
            return self.getToken(MySqlBaseParser.ISOLATION, 0)

        def ISSUER(self):
            return self.getToken(MySqlBaseParser.ISSUER, 0)

        def JSON(self):
            return self.getToken(MySqlBaseParser.JSON, 0)

        def KEY_BLOCK_SIZE(self):
            return self.getToken(MySqlBaseParser.KEY_BLOCK_SIZE, 0)

        def LANGUAGE(self):
            return self.getToken(MySqlBaseParser.LANGUAGE, 0)

        def LAST(self):
            return self.getToken(MySqlBaseParser.LAST, 0)

        def LEAVES(self):
            return self.getToken(MySqlBaseParser.LEAVES, 0)

        def LESS(self):
            return self.getToken(MySqlBaseParser.LESS, 0)

        def LEVEL(self):
            return self.getToken(MySqlBaseParser.LEVEL, 0)

        def LIST(self):
            return self.getToken(MySqlBaseParser.LIST, 0)

        def LOCAL(self):
            return self.getToken(MySqlBaseParser.LOCAL, 0)

        def LOGFILE(self):
            return self.getToken(MySqlBaseParser.LOGFILE, 0)

        def LOGS(self):
            return self.getToken(MySqlBaseParser.LOGS, 0)

        def MASTER(self):
            return self.getToken(MySqlBaseParser.MASTER, 0)

        def MASTER_AUTO_POSITION(self):
            return self.getToken(MySqlBaseParser.MASTER_AUTO_POSITION, 0)

        def MASTER_CONNECT_RETRY(self):
            return self.getToken(MySqlBaseParser.MASTER_CONNECT_RETRY, 0)

        def MASTER_DELAY(self):
            return self.getToken(MySqlBaseParser.MASTER_DELAY, 0)

        def MASTER_HEARTBEAT_PERIOD(self):
            return self.getToken(MySqlBaseParser.MASTER_HEARTBEAT_PERIOD, 0)

        def MASTER_HOST(self):
            return self.getToken(MySqlBaseParser.MASTER_HOST, 0)

        def MASTER_LOG_FILE(self):
            return self.getToken(MySqlBaseParser.MASTER_LOG_FILE, 0)

        def MASTER_LOG_POS(self):
            return self.getToken(MySqlBaseParser.MASTER_LOG_POS, 0)

        def MASTER_PASSWORD(self):
            return self.getToken(MySqlBaseParser.MASTER_PASSWORD, 0)

        def MASTER_PORT(self):
            return self.getToken(MySqlBaseParser.MASTER_PORT, 0)

        def MASTER_RETRY_COUNT(self):
            return self.getToken(MySqlBaseParser.MASTER_RETRY_COUNT, 0)

        def MASTER_SSL(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL, 0)

        def MASTER_SSL_CA(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL_CA, 0)

        def MASTER_SSL_CAPATH(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL_CAPATH, 0)

        def MASTER_SSL_CERT(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL_CERT, 0)

        def MASTER_SSL_CIPHER(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL_CIPHER, 0)

        def MASTER_SSL_CRL(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL_CRL, 0)

        def MASTER_SSL_CRLPATH(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL_CRLPATH, 0)

        def MASTER_SSL_KEY(self):
            return self.getToken(MySqlBaseParser.MASTER_SSL_KEY, 0)

        def MASTER_TLS_VERSION(self):
            return self.getToken(MySqlBaseParser.MASTER_TLS_VERSION, 0)

        def MASTER_USER(self):
            return self.getToken(MySqlBaseParser.MASTER_USER, 0)

        def MAX_CONNECTIONS_PER_HOUR(self):
            return self.getToken(MySqlBaseParser.MAX_CONNECTIONS_PER_HOUR, 0)

        def MAX_QUERIES_PER_HOUR(self):
            return self.getToken(MySqlBaseParser.MAX_QUERIES_PER_HOUR, 0)

        def MAX(self):
            return self.getToken(MySqlBaseParser.MAX, 0)

        def MAX_ROWS(self):
            return self.getToken(MySqlBaseParser.MAX_ROWS, 0)

        def MAX_SIZE(self):
            return self.getToken(MySqlBaseParser.MAX_SIZE, 0)

        def MAX_UPDATES_PER_HOUR(self):
            return self.getToken(MySqlBaseParser.MAX_UPDATES_PER_HOUR, 0)

        def MAX_USER_CONNECTIONS(self):
            return self.getToken(MySqlBaseParser.MAX_USER_CONNECTIONS, 0)

        def MEDIUM(self):
            return self.getToken(MySqlBaseParser.MEDIUM, 0)

        def MEMBER(self):
            return self.getToken(MySqlBaseParser.MEMBER, 0)

        def MEMORY(self):
            return self.getToken(MySqlBaseParser.MEMORY, 0)

        def MERGE(self):
            return self.getToken(MySqlBaseParser.MERGE, 0)

        def MESSAGE_TEXT(self):
            return self.getToken(MySqlBaseParser.MESSAGE_TEXT, 0)

        def MID(self):
            return self.getToken(MySqlBaseParser.MID, 0)

        def MIGRATE(self):
            return self.getToken(MySqlBaseParser.MIGRATE, 0)

        def MIN(self):
            return self.getToken(MySqlBaseParser.MIN, 0)

        def MIN_ROWS(self):
            return self.getToken(MySqlBaseParser.MIN_ROWS, 0)

        def MODE(self):
            return self.getToken(MySqlBaseParser.MODE, 0)

        def MODIFY(self):
            return self.getToken(MySqlBaseParser.MODIFY, 0)

        def MUTEX(self):
            return self.getToken(MySqlBaseParser.MUTEX, 0)

        def MYSQL(self):
            return self.getToken(MySqlBaseParser.MYSQL, 0)

        def MYSQL_ERRNO(self):
            return self.getToken(MySqlBaseParser.MYSQL_ERRNO, 0)

        def NAME(self):
            return self.getToken(MySqlBaseParser.NAME, 0)

        def NAMES(self):
            return self.getToken(MySqlBaseParser.NAMES, 0)

        def NCHAR(self):
            return self.getToken(MySqlBaseParser.NCHAR, 0)

        def NDB_STORED_USER(self):
            return self.getToken(MySqlBaseParser.NDB_STORED_USER, 0)

        def NEVER(self):
            return self.getToken(MySqlBaseParser.NEVER, 0)

        def NEXT(self):
            return self.getToken(MySqlBaseParser.NEXT, 0)

        def NO(self):
            return self.getToken(MySqlBaseParser.NO, 0)

        def NODEGROUP(self):
            return self.getToken(MySqlBaseParser.NODEGROUP, 0)

        def NONE(self):
            return self.getToken(MySqlBaseParser.NONE, 0)

        def NUMBER(self):
            return self.getToken(MySqlBaseParser.NUMBER, 0)

        def OFFLINE(self):
            return self.getToken(MySqlBaseParser.OFFLINE, 0)

        def ODBC(self):
            return self.getToken(MySqlBaseParser.ODBC, 0)

        def OFFSET(self):
            return self.getToken(MySqlBaseParser.OFFSET, 0)

        def OF(self):
            return self.getToken(MySqlBaseParser.OF, 0)

        def OJ(self):
            return self.getToken(MySqlBaseParser.OJ, 0)

        def OLD_PASSWORD(self):
            return self.getToken(MySqlBaseParser.OLD_PASSWORD, 0)

        def ONE(self):
            return self.getToken(MySqlBaseParser.ONE, 0)

        def ONLINE(self):
            return self.getToken(MySqlBaseParser.ONLINE, 0)

        def ONLY(self):
            return self.getToken(MySqlBaseParser.ONLY, 0)

        def OPEN(self):
            return self.getToken(MySqlBaseParser.OPEN, 0)

        def OPTIMIZER_COSTS(self):
            return self.getToken(MySqlBaseParser.OPTIMIZER_COSTS, 0)

        def OPTIONAL(self):
            return self.getToken(MySqlBaseParser.OPTIONAL, 0)

        def OPTIONS(self):
            return self.getToken(MySqlBaseParser.OPTIONS, 0)

        def ORDER(self):
            return self.getToken(MySqlBaseParser.ORDER, 0)

        def OWNER(self):
            return self.getToken(MySqlBaseParser.OWNER, 0)

        def PACK_KEYS(self):
            return self.getToken(MySqlBaseParser.PACK_KEYS, 0)

        def PAGE(self):
            return self.getToken(MySqlBaseParser.PAGE, 0)

        def PARSER(self):
            return self.getToken(MySqlBaseParser.PARSER, 0)

        def PARTIAL(self):
            return self.getToken(MySqlBaseParser.PARTIAL, 0)

        def PARTITIONING(self):
            return self.getToken(MySqlBaseParser.PARTITIONING, 0)

        def PARTITIONS(self):
            return self.getToken(MySqlBaseParser.PARTITIONS, 0)

        def PASSWORD(self):
            return self.getToken(MySqlBaseParser.PASSWORD, 0)

        def PERSIST_RO_VARIABLES_ADMIN(self):
            return self.getToken(MySqlBaseParser.PERSIST_RO_VARIABLES_ADMIN, 0)

        def PHASE(self):
            return self.getToken(MySqlBaseParser.PHASE, 0)

        def PLUGINS(self):
            return self.getToken(MySqlBaseParser.PLUGINS, 0)

        def PLUGIN_DIR(self):
            return self.getToken(MySqlBaseParser.PLUGIN_DIR, 0)

        def PLUGIN(self):
            return self.getToken(MySqlBaseParser.PLUGIN, 0)

        def PORT(self):
            return self.getToken(MySqlBaseParser.PORT, 0)

        def PRECEDES(self):
            return self.getToken(MySqlBaseParser.PRECEDES, 0)

        def PREPARE(self):
            return self.getToken(MySqlBaseParser.PREPARE, 0)

        def PRESERVE(self):
            return self.getToken(MySqlBaseParser.PRESERVE, 0)

        def PREV(self):
            return self.getToken(MySqlBaseParser.PREV, 0)

        def PROCESSLIST(self):
            return self.getToken(MySqlBaseParser.PROCESSLIST, 0)

        def PROFILE(self):
            return self.getToken(MySqlBaseParser.PROFILE, 0)

        def PROFILES(self):
            return self.getToken(MySqlBaseParser.PROFILES, 0)

        def PROXY(self):
            return self.getToken(MySqlBaseParser.PROXY, 0)

        def QUERY(self):
            return self.getToken(MySqlBaseParser.QUERY, 0)

        def QUICK(self):
            return self.getToken(MySqlBaseParser.QUICK, 0)

        def REBUILD(self):
            return self.getToken(MySqlBaseParser.REBUILD, 0)

        def RECOVER(self):
            return self.getToken(MySqlBaseParser.RECOVER, 0)

        def REDO_BUFFER_SIZE(self):
            return self.getToken(MySqlBaseParser.REDO_BUFFER_SIZE, 0)

        def REDUNDANT(self):
            return self.getToken(MySqlBaseParser.REDUNDANT, 0)

        def RELAY(self):
            return self.getToken(MySqlBaseParser.RELAY, 0)

        def RELAYLOG(self):
            return self.getToken(MySqlBaseParser.RELAYLOG, 0)

        def RELAY_LOG_FILE(self):
            return self.getToken(MySqlBaseParser.RELAY_LOG_FILE, 0)

        def RELAY_LOG_POS(self):
            return self.getToken(MySqlBaseParser.RELAY_LOG_POS, 0)

        def REMOVE(self):
            return self.getToken(MySqlBaseParser.REMOVE, 0)

        def REORGANIZE(self):
            return self.getToken(MySqlBaseParser.REORGANIZE, 0)

        def REPAIR(self):
            return self.getToken(MySqlBaseParser.REPAIR, 0)

        def REPLICATE_DO_DB(self):
            return self.getToken(MySqlBaseParser.REPLICATE_DO_DB, 0)

        def REPLICATE_DO_TABLE(self):
            return self.getToken(MySqlBaseParser.REPLICATE_DO_TABLE, 0)

        def REPLICATE_IGNORE_DB(self):
            return self.getToken(MySqlBaseParser.REPLICATE_IGNORE_DB, 0)

        def REPLICATE_IGNORE_TABLE(self):
            return self.getToken(MySqlBaseParser.REPLICATE_IGNORE_TABLE, 0)

        def REPLICATE_REWRITE_DB(self):
            return self.getToken(MySqlBaseParser.REPLICATE_REWRITE_DB, 0)

        def REPLICATE_WILD_DO_TABLE(self):
            return self.getToken(MySqlBaseParser.REPLICATE_WILD_DO_TABLE, 0)

        def REPLICATE_WILD_IGNORE_TABLE(self):
            return self.getToken(MySqlBaseParser.REPLICATE_WILD_IGNORE_TABLE, 0)

        def REPLICATION(self):
            return self.getToken(MySqlBaseParser.REPLICATION, 0)

        def REPLICATION_APPLIER(self):
            return self.getToken(MySqlBaseParser.REPLICATION_APPLIER, 0)

        def REPLICATION_SLAVE_ADMIN(self):
            return self.getToken(MySqlBaseParser.REPLICATION_SLAVE_ADMIN, 0)

        def RESET(self):
            return self.getToken(MySqlBaseParser.RESET, 0)

        def RESOURCE_GROUP_ADMIN(self):
            return self.getToken(MySqlBaseParser.RESOURCE_GROUP_ADMIN, 0)

        def RESOURCE_GROUP_USER(self):
            return self.getToken(MySqlBaseParser.RESOURCE_GROUP_USER, 0)

        def RESUME(self):
            return self.getToken(MySqlBaseParser.RESUME, 0)

        def RETURNED_SQLSTATE(self):
            return self.getToken(MySqlBaseParser.RETURNED_SQLSTATE, 0)

        def RETURNS(self):
            return self.getToken(MySqlBaseParser.RETURNS, 0)

        def ROLE(self):
            return self.getToken(MySqlBaseParser.ROLE, 0)

        def ROLE_ADMIN(self):
            return self.getToken(MySqlBaseParser.ROLE_ADMIN, 0)

        def ROLLBACK(self):
            return self.getToken(MySqlBaseParser.ROLLBACK, 0)

        def ROLLUP(self):
            return self.getToken(MySqlBaseParser.ROLLUP, 0)

        def ROTATE(self):
            return self.getToken(MySqlBaseParser.ROTATE, 0)

        def ROW(self):
            return self.getToken(MySqlBaseParser.ROW, 0)

        def ROWS(self):
            return self.getToken(MySqlBaseParser.ROWS, 0)

        def ROW_FORMAT(self):
            return self.getToken(MySqlBaseParser.ROW_FORMAT, 0)

        def SAVEPOINT(self):
            return self.getToken(MySqlBaseParser.SAVEPOINT, 0)

        def SCHEDULE(self):
            return self.getToken(MySqlBaseParser.SCHEDULE, 0)

        def SCHEMA_NAME(self):
            return self.getToken(MySqlBaseParser.SCHEMA_NAME, 0)

        def SECURITY(self):
            return self.getToken(MySqlBaseParser.SECURITY, 0)

        def SERIAL(self):
            return self.getToken(MySqlBaseParser.SERIAL, 0)

        def SERVER(self):
            return self.getToken(MySqlBaseParser.SERVER, 0)

        def SESSION(self):
            return self.getToken(MySqlBaseParser.SESSION, 0)

        def SESSION_VARIABLES_ADMIN(self):
            return self.getToken(MySqlBaseParser.SESSION_VARIABLES_ADMIN, 0)

        def SET_USER_ID(self):
            return self.getToken(MySqlBaseParser.SET_USER_ID, 0)

        def SHARE(self):
            return self.getToken(MySqlBaseParser.SHARE, 0)

        def SHARED(self):
            return self.getToken(MySqlBaseParser.SHARED, 0)

        def SHOW_ROUTINE(self):
            return self.getToken(MySqlBaseParser.SHOW_ROUTINE, 0)

        def SIGNED(self):
            return self.getToken(MySqlBaseParser.SIGNED, 0)

        def SIMPLE(self):
            return self.getToken(MySqlBaseParser.SIMPLE, 0)

        def SLAVE(self):
            return self.getToken(MySqlBaseParser.SLAVE, 0)

        def SLOW(self):
            return self.getToken(MySqlBaseParser.SLOW, 0)

        def SNAPSHOT(self):
            return self.getToken(MySqlBaseParser.SNAPSHOT, 0)

        def SOCKET(self):
            return self.getToken(MySqlBaseParser.SOCKET, 0)

        def SOME(self):
            return self.getToken(MySqlBaseParser.SOME, 0)

        def SONAME(self):
            return self.getToken(MySqlBaseParser.SONAME, 0)

        def SOUNDS(self):
            return self.getToken(MySqlBaseParser.SOUNDS, 0)

        def SOURCE(self):
            return self.getToken(MySqlBaseParser.SOURCE, 0)

        def SQL_AFTER_GTIDS(self):
            return self.getToken(MySqlBaseParser.SQL_AFTER_GTIDS, 0)

        def SQL_AFTER_MTS_GAPS(self):
            return self.getToken(MySqlBaseParser.SQL_AFTER_MTS_GAPS, 0)

        def SQL_BEFORE_GTIDS(self):
            return self.getToken(MySqlBaseParser.SQL_BEFORE_GTIDS, 0)

        def SQL_BUFFER_RESULT(self):
            return self.getToken(MySqlBaseParser.SQL_BUFFER_RESULT, 0)

        def SQL_CACHE(self):
            return self.getToken(MySqlBaseParser.SQL_CACHE, 0)

        def SQL_NO_CACHE(self):
            return self.getToken(MySqlBaseParser.SQL_NO_CACHE, 0)

        def SQL_THREAD(self):
            return self.getToken(MySqlBaseParser.SQL_THREAD, 0)

        def STACKED(self):
            return self.getToken(MySqlBaseParser.STACKED, 0)

        def START(self):
            return self.getToken(MySqlBaseParser.START, 0)

        def STARTS(self):
            return self.getToken(MySqlBaseParser.STARTS, 0)

        def STATS_AUTO_RECALC(self):
            return self.getToken(MySqlBaseParser.STATS_AUTO_RECALC, 0)

        def STATS_PERSISTENT(self):
            return self.getToken(MySqlBaseParser.STATS_PERSISTENT, 0)

        def STATS_SAMPLE_PAGES(self):
            return self.getToken(MySqlBaseParser.STATS_SAMPLE_PAGES, 0)

        def STATUS(self):
            return self.getToken(MySqlBaseParser.STATUS, 0)

        def STD(self):
            return self.getToken(MySqlBaseParser.STD, 0)

        def STDDEV(self):
            return self.getToken(MySqlBaseParser.STDDEV, 0)

        def STDDEV_POP(self):
            return self.getToken(MySqlBaseParser.STDDEV_POP, 0)

        def STDDEV_SAMP(self):
            return self.getToken(MySqlBaseParser.STDDEV_SAMP, 0)

        def STOP(self):
            return self.getToken(MySqlBaseParser.STOP, 0)

        def STORAGE(self):
            return self.getToken(MySqlBaseParser.STORAGE, 0)

        def STRING(self):
            return self.getToken(MySqlBaseParser.STRING, 0)

        def SUBCLASS_ORIGIN(self):
            return self.getToken(MySqlBaseParser.SUBCLASS_ORIGIN, 0)

        def SUBJECT(self):
            return self.getToken(MySqlBaseParser.SUBJECT, 0)

        def SUBPARTITION(self):
            return self.getToken(MySqlBaseParser.SUBPARTITION, 0)

        def SUBPARTITIONS(self):
            return self.getToken(MySqlBaseParser.SUBPARTITIONS, 0)

        def SUM(self):
            return self.getToken(MySqlBaseParser.SUM, 0)

        def SUSPEND(self):
            return self.getToken(MySqlBaseParser.SUSPEND, 0)

        def SWAPS(self):
            return self.getToken(MySqlBaseParser.SWAPS, 0)

        def SWITCHES(self):
            return self.getToken(MySqlBaseParser.SWITCHES, 0)

        def SYSTEM_VARIABLES_ADMIN(self):
            return self.getToken(MySqlBaseParser.SYSTEM_VARIABLES_ADMIN, 0)

        def TABLE_NAME(self):
            return self.getToken(MySqlBaseParser.TABLE_NAME, 0)

        def TABLESPACE(self):
            return self.getToken(MySqlBaseParser.TABLESPACE, 0)

        def TABLE_ENCRYPTION_ADMIN(self):
            return self.getToken(MySqlBaseParser.TABLE_ENCRYPTION_ADMIN, 0)

        def TEMPORARY(self):
            return self.getToken(MySqlBaseParser.TEMPORARY, 0)

        def TEMPTABLE(self):
            return self.getToken(MySqlBaseParser.TEMPTABLE, 0)

        def THAN(self):
            return self.getToken(MySqlBaseParser.THAN, 0)

        def TRADITIONAL(self):
            return self.getToken(MySqlBaseParser.TRADITIONAL, 0)

        def TRANSACTION(self):
            return self.getToken(MySqlBaseParser.TRANSACTION, 0)

        def TRANSACTIONAL(self):
            return self.getToken(MySqlBaseParser.TRANSACTIONAL, 0)

        def TRIGGERS(self):
            return self.getToken(MySqlBaseParser.TRIGGERS, 0)

        def TRUNCATE(self):
            return self.getToken(MySqlBaseParser.TRUNCATE, 0)

        def UNDEFINED(self):
            return self.getToken(MySqlBaseParser.UNDEFINED, 0)

        def UNDOFILE(self):
            return self.getToken(MySqlBaseParser.UNDOFILE, 0)

        def UNDO_BUFFER_SIZE(self):
            return self.getToken(MySqlBaseParser.UNDO_BUFFER_SIZE, 0)

        def UNINSTALL(self):
            return self.getToken(MySqlBaseParser.UNINSTALL, 0)

        def UNKNOWN(self):
            return self.getToken(MySqlBaseParser.UNKNOWN, 0)

        def UNTIL(self):
            return self.getToken(MySqlBaseParser.UNTIL, 0)

        def UPGRADE(self):
            return self.getToken(MySqlBaseParser.UPGRADE, 0)

        def USER(self):
            return self.getToken(MySqlBaseParser.USER, 0)

        def USE_FRM(self):
            return self.getToken(MySqlBaseParser.USE_FRM, 0)

        def USER_RESOURCES(self):
            return self.getToken(MySqlBaseParser.USER_RESOURCES, 0)

        def VALIDATION(self):
            return self.getToken(MySqlBaseParser.VALIDATION, 0)

        def VALUE(self):
            return self.getToken(MySqlBaseParser.VALUE, 0)

        def VAR_POP(self):
            return self.getToken(MySqlBaseParser.VAR_POP, 0)

        def VAR_SAMP(self):
            return self.getToken(MySqlBaseParser.VAR_SAMP, 0)

        def VARIABLES(self):
            return self.getToken(MySqlBaseParser.VARIABLES, 0)

        def VARIANCE(self):
            return self.getToken(MySqlBaseParser.VARIANCE, 0)

        def VERSION_TOKEN_ADMIN(self):
            return self.getToken(MySqlBaseParser.VERSION_TOKEN_ADMIN, 0)

        def VIEW(self):
            return self.getToken(MySqlBaseParser.VIEW, 0)

        def WAIT(self):
            return self.getToken(MySqlBaseParser.WAIT, 0)

        def WARNINGS(self):
            return self.getToken(MySqlBaseParser.WARNINGS, 0)

        def WITHOUT(self):
            return self.getToken(MySqlBaseParser.WITHOUT, 0)

        def WORK(self):
            return self.getToken(MySqlBaseParser.WORK, 0)

        def WRAPPER(self):
            return self.getToken(MySqlBaseParser.WRAPPER, 0)

        def X509(self):
            return self.getToken(MySqlBaseParser.X509, 0)

        def XA(self):
            return self.getToken(MySqlBaseParser.XA, 0)

        def XA_RECOVER_ADMIN(self):
            return self.getToken(MySqlBaseParser.XA_RECOVER_ADMIN, 0)

        def XML(self):
            return self.getToken(MySqlBaseParser.XML, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_keywordsCanBeId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordsCanBeId" ):
                listener.enterKeywordsCanBeId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordsCanBeId" ):
                listener.exitKeywordsCanBeId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywordsCanBeId" ):
                return visitor.visitKeywordsCanBeId(self)
            else:
                return visitor.visitChildren(self)




    def keywordsCanBeId(self):

        localctx = MySqlBaseParser.KeywordsCanBeIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_keywordsCanBeId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            _la = self._input.LA(1)
            if not(((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (MySqlBaseParser.CURRENT - 76)) | (1 << (MySqlBaseParser.DIAGNOSTICS - 76)) | (1 << (MySqlBaseParser.GROUP - 76)))) != 0) or ((((_la - 150)) & ~0x3f) == 0 and ((1 << (_la - 150)) & ((1 << (MySqlBaseParser.NUMBER - 150)) | (1 << (MySqlBaseParser.ORDER - 150)) | (1 << (MySqlBaseParser.STACKED - 150)))) != 0) or ((((_la - 266)) & ~0x3f) == 0 and ((1 << (_la - 266)) & ((1 << (MySqlBaseParser.SERIAL - 266)) | (1 << (MySqlBaseParser.AVG - 266)) | (1 << (MySqlBaseParser.BIT_AND - 266)) | (1 << (MySqlBaseParser.BIT_OR - 266)) | (1 << (MySqlBaseParser.BIT_XOR - 266)) | (1 << (MySqlBaseParser.COUNT - 266)) | (1 << (MySqlBaseParser.GROUP_CONCAT - 266)) | (1 << (MySqlBaseParser.MAX - 266)) | (1 << (MySqlBaseParser.MIN - 266)) | (1 << (MySqlBaseParser.STD - 266)) | (1 << (MySqlBaseParser.STDDEV - 266)) | (1 << (MySqlBaseParser.STDDEV_POP - 266)) | (1 << (MySqlBaseParser.STDDEV_SAMP - 266)) | (1 << (MySqlBaseParser.SUM - 266)) | (1 << (MySqlBaseParser.VAR_POP - 266)) | (1 << (MySqlBaseParser.VAR_SAMP - 266)) | (1 << (MySqlBaseParser.VARIANCE - 266)))) != 0) or ((((_la - 345)) & ~0x3f) == 0 and ((1 << (_la - 345)) & ((1 << (MySqlBaseParser.ACCOUNT - 345)) | (1 << (MySqlBaseParser.ACTION - 345)) | (1 << (MySqlBaseParser.AFTER - 345)) | (1 << (MySqlBaseParser.AGGREGATE - 345)) | (1 << (MySqlBaseParser.ALGORITHM - 345)) | (1 << (MySqlBaseParser.ANY - 345)) | (1 << (MySqlBaseParser.AT - 345)) | (1 << (MySqlBaseParser.AUTHORS - 345)) | (1 << (MySqlBaseParser.AUTOCOMMIT - 345)) | (1 << (MySqlBaseParser.AUTOEXTEND_SIZE - 345)) | (1 << (MySqlBaseParser.AUTO_INCREMENT - 345)) | (1 << (MySqlBaseParser.AVG_ROW_LENGTH - 345)) | (1 << (MySqlBaseParser.BEGIN - 345)) | (1 << (MySqlBaseParser.BINLOG - 345)) | (1 << (MySqlBaseParser.BIT - 345)) | (1 << (MySqlBaseParser.BLOCK - 345)) | (1 << (MySqlBaseParser.BOOL - 345)) | (1 << (MySqlBaseParser.BOOLEAN - 345)) | (1 << (MySqlBaseParser.BTREE - 345)) | (1 << (MySqlBaseParser.CACHE - 345)) | (1 << (MySqlBaseParser.CASCADED - 345)) | (1 << (MySqlBaseParser.CHAIN - 345)) | (1 << (MySqlBaseParser.CHANGED - 345)) | (1 << (MySqlBaseParser.CHANNEL - 345)) | (1 << (MySqlBaseParser.CHECKSUM - 345)) | (1 << (MySqlBaseParser.PAGE_CHECKSUM - 345)) | (1 << (MySqlBaseParser.CIPHER - 345)) | (1 << (MySqlBaseParser.CLASS_ORIGIN - 345)) | (1 << (MySqlBaseParser.CLIENT - 345)) | (1 << (MySqlBaseParser.CLOSE - 345)) | (1 << (MySqlBaseParser.COALESCE - 345)) | (1 << (MySqlBaseParser.CODE - 345)) | (1 << (MySqlBaseParser.COLUMNS - 345)) | (1 << (MySqlBaseParser.COLUMN_FORMAT - 345)) | (1 << (MySqlBaseParser.COLUMN_NAME - 345)) | (1 << (MySqlBaseParser.COMMENT - 345)) | (1 << (MySqlBaseParser.COMMIT - 345)) | (1 << (MySqlBaseParser.COMPACT - 345)) | (1 << (MySqlBaseParser.COMPLETION - 345)) | (1 << (MySqlBaseParser.COMPRESSED - 345)) | (1 << (MySqlBaseParser.COMPRESSION - 345)) | (1 << (MySqlBaseParser.CONCURRENT - 345)) | (1 << (MySqlBaseParser.CONNECT - 345)) | (1 << (MySqlBaseParser.CONNECTION - 345)) | (1 << (MySqlBaseParser.CONSISTENT - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_CATALOG - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_SCHEMA - 345)) | (1 << (MySqlBaseParser.CONSTRAINT_NAME - 345)) | (1 << (MySqlBaseParser.CONTAINS - 345)) | (1 << (MySqlBaseParser.CONTEXT - 345)) | (1 << (MySqlBaseParser.CONTRIBUTORS - 345)) | (1 << (MySqlBaseParser.COPY - 345)) | (1 << (MySqlBaseParser.CPU - 345)) | (1 << (MySqlBaseParser.CURSOR_NAME - 345)) | (1 << (MySqlBaseParser.DATA - 345)) | (1 << (MySqlBaseParser.DATAFILE - 345)) | (1 << (MySqlBaseParser.DEALLOCATE - 345)) | (1 << (MySqlBaseParser.DEFAULT_AUTH - 345)) | (1 << (MySqlBaseParser.DEFINER - 345)) | (1 << (MySqlBaseParser.DELAY_KEY_WRITE - 345)) | (1 << (MySqlBaseParser.DES_KEY_FILE - 345)) | (1 << (MySqlBaseParser.DIRECTORY - 345)) | (1 << (MySqlBaseParser.DISABLE - 345)) | (1 << (MySqlBaseParser.DISCARD - 345)))) != 0) or ((((_la - 409)) & ~0x3f) == 0 and ((1 << (_la - 409)) & ((1 << (MySqlBaseParser.DISK - 409)) | (1 << (MySqlBaseParser.DO - 409)) | (1 << (MySqlBaseParser.DUMPFILE - 409)) | (1 << (MySqlBaseParser.DUPLICATE - 409)) | (1 << (MySqlBaseParser.DYNAMIC - 409)) | (1 << (MySqlBaseParser.ENABLE - 409)) | (1 << (MySqlBaseParser.ENCRYPTION - 409)) | (1 << (MySqlBaseParser.END - 409)) | (1 << (MySqlBaseParser.ENDS - 409)) | (1 << (MySqlBaseParser.ENGINE - 409)) | (1 << (MySqlBaseParser.ENGINES - 409)) | (1 << (MySqlBaseParser.ERROR - 409)) | (1 << (MySqlBaseParser.ERRORS - 409)) | (1 << (MySqlBaseParser.ESCAPE - 409)) | (1 << (MySqlBaseParser.EVEN - 409)) | (1 << (MySqlBaseParser.EVENT - 409)) | (1 << (MySqlBaseParser.EVENTS - 409)) | (1 << (MySqlBaseParser.EVERY - 409)) | (1 << (MySqlBaseParser.EXCHANGE - 409)) | (1 << (MySqlBaseParser.EXCLUSIVE - 409)) | (1 << (MySqlBaseParser.EXPIRE - 409)) | (1 << (MySqlBaseParser.EXPORT - 409)) | (1 << (MySqlBaseParser.EXTENDED - 409)) | (1 << (MySqlBaseParser.EXTENT_SIZE - 409)) | (1 << (MySqlBaseParser.FAST - 409)) | (1 << (MySqlBaseParser.FAULTS - 409)) | (1 << (MySqlBaseParser.FIELDS - 409)) | (1 << (MySqlBaseParser.FILE_BLOCK_SIZE - 409)) | (1 << (MySqlBaseParser.FILTER - 409)) | (1 << (MySqlBaseParser.FIRST - 409)) | (1 << (MySqlBaseParser.FIXED - 409)) | (1 << (MySqlBaseParser.FLUSH - 409)) | (1 << (MySqlBaseParser.FOLLOWS - 409)) | (1 << (MySqlBaseParser.FOUND - 409)) | (1 << (MySqlBaseParser.FULL - 409)) | (1 << (MySqlBaseParser.FUNCTION - 409)) | (1 << (MySqlBaseParser.GENERAL - 409)) | (1 << (MySqlBaseParser.GLOBAL - 409)) | (1 << (MySqlBaseParser.GRANTS - 409)) | (1 << (MySqlBaseParser.GROUP_REPLICATION - 409)) | (1 << (MySqlBaseParser.HANDLER - 409)) | (1 << (MySqlBaseParser.HASH - 409)) | (1 << (MySqlBaseParser.HELP - 409)) | (1 << (MySqlBaseParser.HOST - 409)) | (1 << (MySqlBaseParser.HOSTS - 409)) | (1 << (MySqlBaseParser.IDENTIFIED - 409)) | (1 << (MySqlBaseParser.IGNORE_SERVER_IDS - 409)) | (1 << (MySqlBaseParser.IMPORT - 409)) | (1 << (MySqlBaseParser.INDEXES - 409)) | (1 << (MySqlBaseParser.INITIAL_SIZE - 409)) | (1 << (MySqlBaseParser.INPLACE - 409)) | (1 << (MySqlBaseParser.INSERT_METHOD - 409)) | (1 << (MySqlBaseParser.INSTALL - 409)) | (1 << (MySqlBaseParser.INSTANCE - 409)) | (1 << (MySqlBaseParser.INVOKER - 409)) | (1 << (MySqlBaseParser.IO - 409)) | (1 << (MySqlBaseParser.IO_THREAD - 409)) | (1 << (MySqlBaseParser.IPC - 409)) | (1 << (MySqlBaseParser.ISOLATION - 409)) | (1 << (MySqlBaseParser.ISSUER - 409)) | (1 << (MySqlBaseParser.JSON - 409)) | (1 << (MySqlBaseParser.KEY_BLOCK_SIZE - 409)) | (1 << (MySqlBaseParser.LANGUAGE - 409)))) != 0) or ((((_la - 473)) & ~0x3f) == 0 and ((1 << (_la - 473)) & ((1 << (MySqlBaseParser.LAST - 473)) | (1 << (MySqlBaseParser.LEAVES - 473)) | (1 << (MySqlBaseParser.LESS - 473)) | (1 << (MySqlBaseParser.LEVEL - 473)) | (1 << (MySqlBaseParser.LIST - 473)) | (1 << (MySqlBaseParser.LOCAL - 473)) | (1 << (MySqlBaseParser.LOGFILE - 473)) | (1 << (MySqlBaseParser.LOGS - 473)) | (1 << (MySqlBaseParser.MASTER - 473)) | (1 << (MySqlBaseParser.MASTER_AUTO_POSITION - 473)) | (1 << (MySqlBaseParser.MASTER_CONNECT_RETRY - 473)) | (1 << (MySqlBaseParser.MASTER_DELAY - 473)) | (1 << (MySqlBaseParser.MASTER_HEARTBEAT_PERIOD - 473)) | (1 << (MySqlBaseParser.MASTER_HOST - 473)) | (1 << (MySqlBaseParser.MASTER_LOG_FILE - 473)) | (1 << (MySqlBaseParser.MASTER_LOG_POS - 473)) | (1 << (MySqlBaseParser.MASTER_PASSWORD - 473)) | (1 << (MySqlBaseParser.MASTER_PORT - 473)) | (1 << (MySqlBaseParser.MASTER_RETRY_COUNT - 473)) | (1 << (MySqlBaseParser.MASTER_SSL - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CA - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CAPATH - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CERT - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CIPHER - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CRL - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_CRLPATH - 473)) | (1 << (MySqlBaseParser.MASTER_SSL_KEY - 473)) | (1 << (MySqlBaseParser.MASTER_TLS_VERSION - 473)) | (1 << (MySqlBaseParser.MASTER_USER - 473)) | (1 << (MySqlBaseParser.MAX_CONNECTIONS_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_QUERIES_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_ROWS - 473)) | (1 << (MySqlBaseParser.MAX_SIZE - 473)) | (1 << (MySqlBaseParser.MAX_UPDATES_PER_HOUR - 473)) | (1 << (MySqlBaseParser.MAX_USER_CONNECTIONS - 473)) | (1 << (MySqlBaseParser.MEDIUM - 473)) | (1 << (MySqlBaseParser.MEMBER - 473)) | (1 << (MySqlBaseParser.MERGE - 473)) | (1 << (MySqlBaseParser.MESSAGE_TEXT - 473)) | (1 << (MySqlBaseParser.MID - 473)) | (1 << (MySqlBaseParser.MIGRATE - 473)) | (1 << (MySqlBaseParser.MIN_ROWS - 473)) | (1 << (MySqlBaseParser.MODE - 473)) | (1 << (MySqlBaseParser.MODIFY - 473)) | (1 << (MySqlBaseParser.MUTEX - 473)) | (1 << (MySqlBaseParser.MYSQL - 473)) | (1 << (MySqlBaseParser.MYSQL_ERRNO - 473)) | (1 << (MySqlBaseParser.NAME - 473)) | (1 << (MySqlBaseParser.NAMES - 473)) | (1 << (MySqlBaseParser.NCHAR - 473)) | (1 << (MySqlBaseParser.NEVER - 473)) | (1 << (MySqlBaseParser.NEXT - 473)) | (1 << (MySqlBaseParser.NO - 473)) | (1 << (MySqlBaseParser.NODEGROUP - 473)) | (1 << (MySqlBaseParser.NONE - 473)) | (1 << (MySqlBaseParser.ODBC - 473)) | (1 << (MySqlBaseParser.OFFLINE - 473)) | (1 << (MySqlBaseParser.OFFSET - 473)) | (1 << (MySqlBaseParser.OF - 473)) | (1 << (MySqlBaseParser.OJ - 473)) | (1 << (MySqlBaseParser.OLD_PASSWORD - 473)) | (1 << (MySqlBaseParser.ONE - 473)) | (1 << (MySqlBaseParser.ONLINE - 473)) | (1 << (MySqlBaseParser.ONLY - 473)))) != 0) or ((((_la - 537)) & ~0x3f) == 0 and ((1 << (_la - 537)) & ((1 << (MySqlBaseParser.OPEN - 537)) | (1 << (MySqlBaseParser.OPTIMIZER_COSTS - 537)) | (1 << (MySqlBaseParser.OPTIONS - 537)) | (1 << (MySqlBaseParser.OWNER - 537)) | (1 << (MySqlBaseParser.PACK_KEYS - 537)) | (1 << (MySqlBaseParser.PAGE - 537)) | (1 << (MySqlBaseParser.PARSER - 537)) | (1 << (MySqlBaseParser.PARTIAL - 537)) | (1 << (MySqlBaseParser.PARTITIONING - 537)) | (1 << (MySqlBaseParser.PARTITIONS - 537)) | (1 << (MySqlBaseParser.PASSWORD - 537)) | (1 << (MySqlBaseParser.PHASE - 537)) | (1 << (MySqlBaseParser.PLUGIN - 537)) | (1 << (MySqlBaseParser.PLUGIN_DIR - 537)) | (1 << (MySqlBaseParser.PLUGINS - 537)) | (1 << (MySqlBaseParser.PORT - 537)) | (1 << (MySqlBaseParser.PRECEDES - 537)) | (1 << (MySqlBaseParser.PREPARE - 537)) | (1 << (MySqlBaseParser.PRESERVE - 537)) | (1 << (MySqlBaseParser.PREV - 537)) | (1 << (MySqlBaseParser.PROCESSLIST - 537)) | (1 << (MySqlBaseParser.PROFILE - 537)) | (1 << (MySqlBaseParser.PROFILES - 537)) | (1 << (MySqlBaseParser.PROXY - 537)) | (1 << (MySqlBaseParser.QUERY - 537)) | (1 << (MySqlBaseParser.QUICK - 537)) | (1 << (MySqlBaseParser.REBUILD - 537)) | (1 << (MySqlBaseParser.RECOVER - 537)) | (1 << (MySqlBaseParser.REDO_BUFFER_SIZE - 537)) | (1 << (MySqlBaseParser.REDUNDANT - 537)) | (1 << (MySqlBaseParser.RELAY - 537)) | (1 << (MySqlBaseParser.RELAY_LOG_FILE - 537)) | (1 << (MySqlBaseParser.RELAY_LOG_POS - 537)) | (1 << (MySqlBaseParser.RELAYLOG - 537)) | (1 << (MySqlBaseParser.REMOVE - 537)) | (1 << (MySqlBaseParser.REORGANIZE - 537)) | (1 << (MySqlBaseParser.REPAIR - 537)) | (1 << (MySqlBaseParser.REPLICATE_DO_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_DO_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_IGNORE_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_IGNORE_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_REWRITE_DB - 537)) | (1 << (MySqlBaseParser.REPLICATE_WILD_DO_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATE_WILD_IGNORE_TABLE - 537)) | (1 << (MySqlBaseParser.REPLICATION - 537)) | (1 << (MySqlBaseParser.RESET - 537)) | (1 << (MySqlBaseParser.RESUME - 537)) | (1 << (MySqlBaseParser.RETURNED_SQLSTATE - 537)) | (1 << (MySqlBaseParser.RETURNS - 537)) | (1 << (MySqlBaseParser.ROLE - 537)) | (1 << (MySqlBaseParser.ROLLBACK - 537)) | (1 << (MySqlBaseParser.ROLLUP - 537)) | (1 << (MySqlBaseParser.ROTATE - 537)) | (1 << (MySqlBaseParser.ROW - 537)) | (1 << (MySqlBaseParser.ROWS - 537)) | (1 << (MySqlBaseParser.ROW_FORMAT - 537)) | (1 << (MySqlBaseParser.SAVEPOINT - 537)) | (1 << (MySqlBaseParser.SCHEDULE - 537)) | (1 << (MySqlBaseParser.SECURITY - 537)) | (1 << (MySqlBaseParser.SERVER - 537)) | (1 << (MySqlBaseParser.SESSION - 537)) | (1 << (MySqlBaseParser.SHARE - 537)) | (1 << (MySqlBaseParser.SHARED - 537)))) != 0) or ((((_la - 601)) & ~0x3f) == 0 and ((1 << (_la - 601)) & ((1 << (MySqlBaseParser.SIGNED - 601)) | (1 << (MySqlBaseParser.SIMPLE - 601)) | (1 << (MySqlBaseParser.SLAVE - 601)) | (1 << (MySqlBaseParser.SLOW - 601)) | (1 << (MySqlBaseParser.SNAPSHOT - 601)) | (1 << (MySqlBaseParser.SOCKET - 601)) | (1 << (MySqlBaseParser.SOME - 601)) | (1 << (MySqlBaseParser.SONAME - 601)) | (1 << (MySqlBaseParser.SOUNDS - 601)) | (1 << (MySqlBaseParser.SOURCE - 601)) | (1 << (MySqlBaseParser.SQL_AFTER_GTIDS - 601)) | (1 << (MySqlBaseParser.SQL_AFTER_MTS_GAPS - 601)) | (1 << (MySqlBaseParser.SQL_BEFORE_GTIDS - 601)) | (1 << (MySqlBaseParser.SQL_BUFFER_RESULT - 601)) | (1 << (MySqlBaseParser.SQL_CACHE - 601)) | (1 << (MySqlBaseParser.SQL_NO_CACHE - 601)) | (1 << (MySqlBaseParser.SQL_THREAD - 601)) | (1 << (MySqlBaseParser.START - 601)) | (1 << (MySqlBaseParser.STARTS - 601)) | (1 << (MySqlBaseParser.STATS_AUTO_RECALC - 601)) | (1 << (MySqlBaseParser.STATS_PERSISTENT - 601)) | (1 << (MySqlBaseParser.STATS_SAMPLE_PAGES - 601)) | (1 << (MySqlBaseParser.STATUS - 601)) | (1 << (MySqlBaseParser.STOP - 601)) | (1 << (MySqlBaseParser.STORAGE - 601)) | (1 << (MySqlBaseParser.STRING - 601)) | (1 << (MySqlBaseParser.SUBCLASS_ORIGIN - 601)) | (1 << (MySqlBaseParser.SUBJECT - 601)) | (1 << (MySqlBaseParser.SUBPARTITION - 601)) | (1 << (MySqlBaseParser.SUBPARTITIONS - 601)) | (1 << (MySqlBaseParser.SUSPEND - 601)) | (1 << (MySqlBaseParser.SWAPS - 601)) | (1 << (MySqlBaseParser.SWITCHES - 601)) | (1 << (MySqlBaseParser.TABLE_NAME - 601)) | (1 << (MySqlBaseParser.TABLESPACE - 601)) | (1 << (MySqlBaseParser.TEMPORARY - 601)) | (1 << (MySqlBaseParser.TEMPTABLE - 601)) | (1 << (MySqlBaseParser.THAN - 601)) | (1 << (MySqlBaseParser.TRADITIONAL - 601)) | (1 << (MySqlBaseParser.TRANSACTION - 601)) | (1 << (MySqlBaseParser.TRANSACTIONAL - 601)) | (1 << (MySqlBaseParser.TRIGGERS - 601)) | (1 << (MySqlBaseParser.TRUNCATE - 601)) | (1 << (MySqlBaseParser.UNDEFINED - 601)) | (1 << (MySqlBaseParser.UNDOFILE - 601)) | (1 << (MySqlBaseParser.UNDO_BUFFER_SIZE - 601)) | (1 << (MySqlBaseParser.UNINSTALL - 601)) | (1 << (MySqlBaseParser.UNKNOWN - 601)) | (1 << (MySqlBaseParser.UNTIL - 601)) | (1 << (MySqlBaseParser.UPGRADE - 601)) | (1 << (MySqlBaseParser.USER - 601)) | (1 << (MySqlBaseParser.USE_FRM - 601)) | (1 << (MySqlBaseParser.USER_RESOURCES - 601)) | (1 << (MySqlBaseParser.VALIDATION - 601)) | (1 << (MySqlBaseParser.VALUE - 601)) | (1 << (MySqlBaseParser.VARIABLES - 601)) | (1 << (MySqlBaseParser.VIEW - 601)) | (1 << (MySqlBaseParser.WAIT - 601)) | (1 << (MySqlBaseParser.WARNINGS - 601)) | (1 << (MySqlBaseParser.WITHOUT - 601)))) != 0) or ((((_la - 665)) & ~0x3f) == 0 and ((1 << (_la - 665)) & ((1 << (MySqlBaseParser.WORK - 665)) | (1 << (MySqlBaseParser.WRAPPER - 665)) | (1 << (MySqlBaseParser.X509 - 665)) | (1 << (MySqlBaseParser.XA - 665)) | (1 << (MySqlBaseParser.XML - 665)) | (1 << (MySqlBaseParser.INTERNAL - 665)) | (1 << (MySqlBaseParser.AUDIT_ADMIN - 665)) | (1 << (MySqlBaseParser.BACKUP_ADMIN - 665)) | (1 << (MySqlBaseParser.BINLOG_ADMIN - 665)) | (1 << (MySqlBaseParser.BINLOG_ENCRYPTION_ADMIN - 665)) | (1 << (MySqlBaseParser.CLONE_ADMIN - 665)) | (1 << (MySqlBaseParser.CONNECTION_ADMIN - 665)) | (1 << (MySqlBaseParser.ENCRYPTION_KEY_ADMIN - 665)) | (1 << (MySqlBaseParser.FIREWALL_ADMIN - 665)) | (1 << (MySqlBaseParser.FIREWALL_USER - 665)) | (1 << (MySqlBaseParser.GROUP_REPLICATION_ADMIN - 665)) | (1 << (MySqlBaseParser.INNODB_REDO_LOG_ARCHIVE - 665)) | (1 << (MySqlBaseParser.NDB_STORED_USER - 665)) | (1 << (MySqlBaseParser.PERSIST_RO_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.REPLICATION_APPLIER - 665)) | (1 << (MySqlBaseParser.REPLICATION_SLAVE_ADMIN - 665)) | (1 << (MySqlBaseParser.RESOURCE_GROUP_ADMIN - 665)) | (1 << (MySqlBaseParser.RESOURCE_GROUP_USER - 665)) | (1 << (MySqlBaseParser.ROLE_ADMIN - 665)) | (1 << (MySqlBaseParser.SESSION_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.SET_USER_ID - 665)) | (1 << (MySqlBaseParser.SHOW_ROUTINE - 665)) | (1 << (MySqlBaseParser.SYSTEM_VARIABLES_ADMIN - 665)) | (1 << (MySqlBaseParser.TABLE_ENCRYPTION_ADMIN - 665)) | (1 << (MySqlBaseParser.VERSION_TOKEN_ADMIN - 665)) | (1 << (MySqlBaseParser.XA_RECOVER_ADMIN - 665)))) != 0) or _la==MySqlBaseParser.MEMORY or _la==MySqlBaseParser.CATALOG_NAME or _la==MySqlBaseParser.SCHEMA_NAME or _la==MySqlBaseParser.OPTIONAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterMarker(self):
            return self.getTypedRuleContext(MySqlBaseParser.ParameterMarkerContext,0)


        def stringLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.StringLiteralContext,0)


        def decimalLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.DecimalLiteralContext,0)


        def MINUS(self):
            return self.getToken(MySqlBaseParser.MINUS, 0)

        def hexadecimalLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.HexadecimalLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.BooleanLiteralContext,0)


        def realLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.RealLiteralContext,0)


        def bitString(self):
            return self.getTypedRuleContext(MySqlBaseParser.BitStringContext,0)


        def nullLiteral(self):
            return self.getTypedRuleContext(MySqlBaseParser.NullLiteralContext,0)


        def getRuleIndex(self):
            return MySqlBaseParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = MySqlBaseParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_constant)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.QUESTION_, MySqlBaseParser.PERCENT_S_, MySqlBaseParser.PERCENT_NAME_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.parameterMarker()
                pass
            elif token in [MySqlBaseParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.stringLiteral()
                pass
            elif token in [MySqlBaseParser.ZERO_DECIMAL, MySqlBaseParser.ONE_DECIMAL, MySqlBaseParser.TWO_DECIMAL, MySqlBaseParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.decimalLiteral()
                pass
            elif token in [MySqlBaseParser.MINUS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 452
                self.match(MySqlBaseParser.MINUS)
                self.state = 453
                self.decimalLiteral()
                pass
            elif token in [MySqlBaseParser.HEXADECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 454
                self.hexadecimalLiteral()
                pass
            elif token in [MySqlBaseParser.FALSE, MySqlBaseParser.TRUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 455
                self.booleanLiteral()
                pass
            elif token in [MySqlBaseParser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 456
                self.realLiteral()
                pass
            elif token in [MySqlBaseParser.BIT_STRING]:
                self.enterOuterAlt(localctx, 8)
                self.state = 457
                self.bitString()
                pass
            elif token in [MySqlBaseParser.NULL_LITERAL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 458
                self.nullLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL_LITERAL(self):
            return self.getToken(MySqlBaseParser.NULL_LITERAL, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_nullLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullLiteral" ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullLiteral" ):
                listener.exitNullLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullLiteral" ):
                return visitor.visitNullLiteral(self)
            else:
                return visitor.visitChildren(self)




    def nullLiteral(self):

        localctx = MySqlBaseParser.NullLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_nullLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(MySqlBaseParser.NULL_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RealLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REAL_LITERAL(self):
            return self.getToken(MySqlBaseParser.REAL_LITERAL, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_realLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealLiteral" ):
                listener.enterRealLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealLiteral" ):
                listener.exitRealLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealLiteral" ):
                return visitor.visitRealLiteral(self)
            else:
                return visitor.visitChildren(self)




    def realLiteral(self):

        localctx = MySqlBaseParser.RealLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_realLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(MySqlBaseParser.REAL_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BIT_STRING(self):
            return self.getToken(MySqlBaseParser.BIT_STRING, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_bitString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitString" ):
                listener.enterBitString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitString" ):
                listener.exitBitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitString" ):
                return visitor.visitBitString(self)
            else:
                return visitor.visitChildren(self)




    def bitString(self):

        localctx = MySqlBaseParser.BitStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_bitString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(MySqlBaseParser.BIT_STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MySqlBaseParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MySqlBaseParser.FALSE, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_booleanLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLiteral" ):
                return visitor.visitBooleanLiteral(self)
            else:
                return visitor.visitChildren(self)




    def booleanLiteral(self):

        localctx = MySqlBaseParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            _la = self._input.LA(1)
            if not(_la==MySqlBaseParser.FALSE or _la==MySqlBaseParser.TRUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(MySqlBaseParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)




    def stringLiteral(self):

        localctx = MySqlBaseParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(MySqlBaseParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecimalLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LITERAL(self):
            return self.getToken(MySqlBaseParser.DECIMAL_LITERAL, 0)

        def ZERO_DECIMAL(self):
            return self.getToken(MySqlBaseParser.ZERO_DECIMAL, 0)

        def ONE_DECIMAL(self):
            return self.getToken(MySqlBaseParser.ONE_DECIMAL, 0)

        def TWO_DECIMAL(self):
            return self.getToken(MySqlBaseParser.TWO_DECIMAL, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_decimalLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalLiteral" ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalLiteral" ):
                listener.exitDecimalLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalLiteral" ):
                return visitor.visitDecimalLiteral(self)
            else:
                return visitor.visitChildren(self)




    def decimalLiteral(self):

        localctx = MySqlBaseParser.DecimalLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_decimalLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlBaseParser.ZERO_DECIMAL) | (1 << MySqlBaseParser.ONE_DECIMAL) | (1 << MySqlBaseParser.TWO_DECIMAL))) != 0) or _la==MySqlBaseParser.DECIMAL_LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HexadecimalLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEXADECIMAL_LITERAL(self):
            return self.getToken(MySqlBaseParser.HEXADECIMAL_LITERAL, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_hexadecimalLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexadecimalLiteral" ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexadecimalLiteral" ):
                listener.exitHexadecimalLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexadecimalLiteral" ):
                return visitor.visitHexadecimalLiteral(self)
            else:
                return visitor.visitChildren(self)




    def hexadecimalLiteral(self):

        localctx = MySqlBaseParser.HexadecimalLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_hexadecimalLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(MySqlBaseParser.HEXADECIMAL_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(MySqlBaseParser.ORDER, 0)

        def BY(self):
            return self.getToken(MySqlBaseParser.BY, 0)

        def orderByExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.OrderByExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.OrderByExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlBaseParser.COMMA)
            else:
                return self.getToken(MySqlBaseParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_orderByClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByClause" ):
                listener.enterOrderByClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByClause" ):
                listener.exitOrderByClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByClause" ):
                return visitor.visitOrderByClause(self)
            else:
                return visitor.visitChildren(self)




    def orderByClause(self):

        localctx = MySqlBaseParser.OrderByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_orderByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(MySqlBaseParser.ORDER)
            self.state = 476
            self.match(MySqlBaseParser.BY)
            self.state = 477
            self.orderByExpression()
            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlBaseParser.COMMA:
                self.state = 478
                self.match(MySqlBaseParser.COMMA)
                self.state = 479
                self.orderByExpression()
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.order = None # Token

        def expression(self):
            return self.getTypedRuleContext(MySqlBaseParser.ExpressionContext,0)


        def ASC(self):
            return self.getToken(MySqlBaseParser.ASC, 0)

        def DESC(self):
            return self.getToken(MySqlBaseParser.DESC, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_orderByExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByExpression" ):
                listener.enterOrderByExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByExpression" ):
                listener.exitOrderByExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByExpression" ):
                return visitor.visitOrderByExpression(self)
            else:
                return visitor.visitChildren(self)




    def orderByExpression(self):

        localctx = MySqlBaseParser.OrderByExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_orderByExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.expression(0)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlBaseParser.ASC or _la==MySqlBaseParser.DESC:
                self.state = 486
                localctx.order = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MySqlBaseParser.ASC or _la==MySqlBaseParser.DESC):
                    localctx.order = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(MySqlBaseParser.LIMIT, 0)

        def decimalLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlBaseParser.DecimalLiteralContext)
            else:
                return self.getTypedRuleContext(MySqlBaseParser.DecimalLiteralContext,i)


        def COMMA(self):
            return self.getToken(MySqlBaseParser.COMMA, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_limitClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitClause" ):
                listener.enterLimitClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitClause" ):
                listener.exitLimitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitClause" ):
                return visitor.visitLimitClause(self)
            else:
                return visitor.visitChildren(self)




    def limitClause(self):

        localctx = MySqlBaseParser.LimitClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_limitClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(MySqlBaseParser.LIMIT)
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlBaseParser.ZERO_DECIMAL) | (1 << MySqlBaseParser.ONE_DECIMAL) | (1 << MySqlBaseParser.TWO_DECIMAL))) != 0) or _la==MySqlBaseParser.DECIMAL_LITERAL:
                    self.state = 490
                    self.decimalLiteral()


                self.state = 493
                self.match(MySqlBaseParser.COMMA)


            self.state = 496
            self.decimalLiteral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LockClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MySqlBaseParser.FOR, 0)

        def UPDATE(self):
            return self.getToken(MySqlBaseParser.UPDATE, 0)

        def LOCK(self):
            return self.getToken(MySqlBaseParser.LOCK, 0)

        def IN(self):
            return self.getToken(MySqlBaseParser.IN, 0)

        def SHARE(self):
            return self.getToken(MySqlBaseParser.SHARE, 0)

        def MODE(self):
            return self.getToken(MySqlBaseParser.MODE, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_lockClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLockClause" ):
                listener.enterLockClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLockClause" ):
                listener.exitLockClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLockClause" ):
                return visitor.visitLockClause(self)
            else:
                return visitor.visitChildren(self)




    def lockClause(self):

        localctx = MySqlBaseParser.LockClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lockClause)
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlBaseParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(MySqlBaseParser.FOR)
                self.state = 499
                self.match(MySqlBaseParser.UPDATE)
                pass
            elif token in [MySqlBaseParser.LOCK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(MySqlBaseParser.LOCK)
                self.state = 501
                self.match(MySqlBaseParser.IN)
                self.state = 502
                self.match(MySqlBaseParser.SHARE)
                self.state = 503
                self.match(MySqlBaseParser.MODE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterMarkerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION_(self):
            return self.getToken(MySqlBaseParser.QUESTION_, 0)

        def PERCENT_S_(self):
            return self.getToken(MySqlBaseParser.PERCENT_S_, 0)

        def PERCENT_NAME_(self):
            return self.getToken(MySqlBaseParser.PERCENT_NAME_, 0)

        def getRuleIndex(self):
            return MySqlBaseParser.RULE_parameterMarker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterMarker" ):
                listener.enterParameterMarker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterMarker" ):
                listener.exitParameterMarker(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterMarker" ):
                return visitor.visitParameterMarker(self)
            else:
                return visitor.visitChildren(self)




    def parameterMarker(self):

        localctx = MySqlBaseParser.ParameterMarkerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_parameterMarker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlBaseParser.QUESTION_) | (1 << MySqlBaseParser.PERCENT_S_) | (1 << MySqlBaseParser.PERCENT_NAME_))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         





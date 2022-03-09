VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Лист1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Option Explicit
Sub prl1()
Dim a, b, c, s As String
a = InputBox("x=")
b = InputBox("y=")
s = "введенные значения: a=" & a & "b=" & b
If a > b Then
c = a
a = b
b = c
End If
s = s & Chr(10) & Chr(13) & "новые значения : a=" & a & "b=" & b
MsgBox s

End Sub

Sub prl2()
Dim a, b, c, d, f As String
a = InputBox("a=")
b = InputBox("b=")
c = InputBox("c=")
d = InputBox("d=")
If a * b > c * d Then f = (a + b + c + d / 4) Else f = (a * b * c * d) ^ 1 / 4
MsgBox f
End Sub

Sub prl3()
Dim a, b, c, d As String
a = InputBox("a=")
b = InputBox("b=")
c = InputBox("c=")
If a + b > c & a + c > b & b + c > a Then d = "можно" Else d = "нельзя"
MsgBox d
End Sub
 Sub prl4()
 Dim q, w, e, r, t, y, u, i As Integer
 q = InputBox("чисел будет:")
 If q = 3 Then
 w = InputBox("w=")
 e = InputBox("e=")
 t = Int(Rnd * 100 + 1)
 If w > e And w > t Then y = w Else If e > w And e > t Then y = e Else y = t
 End If
 If q = 4 Then
 w = InputBox("w=")
 e = InputBox("e=")
 t = Int(Rnd * 100 + 1)
 u = Int(Rnd * 100 + 1)
 If w > e And w > t And w > u Then y = w Else If e > w And e > t And e > u Then y = e Else If t > e And t > w And t > u Then y = t Else y = u
 End If
 If q = 5 Then
 w = InputBox("w=")
 e = InputBox("e=")
 t = Int(Rnd * 100 + 1)
 u = Int(Rnd * 100 + 1)
 i = InputBox("i=")
 If w > e And w > t And w > u And w > i Then y = w Else If e > w And e > t And e > u And e > i Then y = e Else If t > w And t > e And t > u And t > i Then y = t Else If u > w And u > t And u > i And u > e Then y = u Else y = i
 End If
 MsgBox y
 End Sub
Sub prl5()
Dim a, b, c, d As Integer
a = InputBox("a=")
b = InputBox("b=")
c = InputBox("c=")
If Abs(a - b - c) > Abs(b - c - a) And Abs(a - b - c) > Abs(c - a - b) Then d = Abs(a - b - c) Else If Abs(b - a - c) > Abs(c - a - b) And Abs(b - a - c) > Abs(a - b - c) Then d = Abs(b - a - c) Else r = Abs(c - a - b)
End If
MsgBox r
End Sub
Sub prl6()
Dim q, w, e, r, t, y As Integer
q = InputBox("фигура")
If q = ("треугольник") Then
w = Int(InputBox("a="))
e = Int(InputBox("b="))
r = Int(InputBox("c="))
t = (w + e + r)
End If
If q = ("прямоугольник") Then
w = Int(InputBox("a="))
e = Int(InputBox("b="))
r = Int(InputBox("c="))
y = Int(InputBox("d="))
t = w + e + r + y
End If
If q = ("квадрат") Then
w = Int(InputBox("a="))
t = w * 4
End If
If q = ("трапеция") Then
w = Int(InputBox("a="))
e = Int(InputBox("b="))
r = Int(InputBox("c="))
y = Int(InputBox("d="))
t = w + e + r + y
End If
If q = ("ромб") Then
w = Int(InputBox("a="))
e = Int(InputBox("b="))
r = Int(InputBox("c="))
y = Int(InputBox("d="))
t = w + e + r + y
End If
If q = ("круг") Then
w = Int(InputBox("a="))
t = 3.14 * 2 * w
End If
MsgBox t
End Sub

Sub prl7()
Dim a As Integer, b As Variant
a = Int((Rnd * 100) Mod 4)
If a = 0 Then b = ("отрезок")
If a = 1 Then b = ("треугольник")
If a = 2 Then b = ("тропеция,квадрат,ромб,параллелограм,прямоугольник")
If a = 3 Then b = ("пятиугольник")
MsgBox b
End Sub

Sub prl8()
Dim s, a, e, r, t, y As Integer
s = InputBox("введите площадь")
a = InputBox("введите разницу между основанием и высотой")

End Sub

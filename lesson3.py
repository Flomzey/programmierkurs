#lesson3 file made by Flomzey
#
# Mit input() kann man dinge aus der konsole auslesen, wenn etwas eingegeben
# wird kann man es wie eine variable speichern.

input = input()
if input.find("*") >= 0:

    xy = input.split("*") #10*10
    sum = 1
    for x in xy:
        sum = sum * int(x)

    print(sum)

if input.find("+") >= 0:
    xy = input.split("+")
    sum = 0
    for x in xy:
        sum = sum + int(x)
    print(sum)
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celcius_ke_rearmur(celcius):
    return (4/5) * (celcius)

def celcius_ke_kelvin(celcius):
    return celcius + 273

inp = float(input("masukkan suhu celcius "))

reamur = celcius_ke_rearmur(inp)
fahrenheit = celcius_ke_fahrenheit(inp)
kelvin = celcius_ke_kelvin(inp)
 
print(f"suhu reamur = {reamur}")
print(f"suhu fahrenheit = {fahrenheit}")
print(f"suhu ke kelvin = {kelvin}")

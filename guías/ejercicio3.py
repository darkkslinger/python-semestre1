dia=12000
noche=16000
domingodia=dia+2000
domingonoche=noche+3000

trabajadores={
    'Trabajador 1':{
    'Turnos dia':['Jueves','Viernes'],
    'Turnos noche':['Lunes','Martes','Miercoles']
    },
    'Trabajador 2':{
    'Turnos dia':['Domingo'],
    'Turnos noche':['Martes','Miercoles','Jueves']
    },
    'Trabajador 3':{
    'Turnos dia':['Miercoles','Jueves','Viernes'],
    'Turnos noche':['Sábado','Domingo']
    }
}
for i,dias in trabajadores.items():
    totalsemana = 0
    for j in dias['Turnos dia']:
        if j == 'Domingo':
            pagodiario = domingodia*10
        else:
            pagodiario = dia*10
        totalsemana += pagodiario
    for k in dias['Turnos noche']:
        if k == 'Domingo':
            pagodiario = domingonoche*10
        else:
            pagodiario = noche*10
        totalsemana += pagodiario
        
    diastrabajados=len(trabajadores[i]['Turnos dia']) + len(trabajadores[i]['Turnos noche'])
    trabajadores[i]['Pago diario'] = round(totalsemana/diastrabajados)
    trabajadores[i]['Total semanal'] = totalsemana
    
print(f"\nTrabajador 1: {trabajadores['Trabajador 1']}\n")
print(f"\nTrabajador 2: {trabajadores['Trabajador 2']}\n")
print(f"\nTrabajador 3: {trabajadores['Trabajador 3']}\n")
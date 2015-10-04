var material_fields = $('#material_forms')

counter = 1

$('#add_material_btn').click(function(event){
	event.preventDefault()
	counter ++;
	html = '<div>Nombre del material: <input maxlength="255" name="name' + counter + '" type="text">'
			+'<br><br>'
			+'Unidades de medicion: <input maxlength="255" name="unity' + counter + '" type="text">'
			+'<br><br>'
			+'Cantidad que ocupa: <input name="quantity' + counter + '" type="number">'
			+'<br><br>'
			+'Costo al que se compra: <input name="cost' + counter + '" type="number">'
			+'<br><br></div>'

	material_fields.append(html)
})

material_fields.append('<div>Nombre del material: <input maxlength="255" name="name' + counter + '" type="text">'
			+'<br><br>'
			+'Unidades de medicion: <input maxlength="255" name="unity' + counter + '" type="text">'
			+'<br><br>'
			+'Cantidad que ocupa: <input name="quantity' + counter + '" type="number">'
			+'<br><br>'
			+'Costo al que se compra: <input name="cost' + counter + '" type="number">'
			+'<br><br></div>')
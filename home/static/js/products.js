var material_fields = $('#material_forms')

counter = 1

$('#add_material_btn').click(function(event){
	event.preventDefault()
	counter ++;
	html = '<div>Name: <input maxlength="255" name="name' + counter + '" type="text">'
			+'<br><br>'
			+'Unity: <input maxlength="255" name="unity' + counter + '" type="text">'
			+'<br><br>'
			+'Quantity: <input name="quantity' + counter + '" type="number">'
			+'<br><br>'
			+'Cost: <input name="cost' + counter + '" type="number">'
			+'<br><br></div>'

	material_fields.append(html)
})

material_fields.append('<div>Name: <input maxlength="255" name="name' + counter + '" type="text">'
			+'<br><br>'
			+'Unity: <input maxlength="255" name="unity' + counter + '" type="text">'
			+'<br><br>'
			+'Quantity: <input name="quantity' + counter + '" type="number">'
			+'<br><br>'
			+'Cost: <input name="cost' + counter + '" type="number">'
			+'<br><br></div>')
layer = iface.activeLayer()

def criarCampo (nomeCampo, tipoCampo, comprimento, precisao):

	indiceCampo = layer.fields().indexOf(nomeCampo)

	if indiceCampo == -1:

		provedor = layer.dataProvider()
		provedor.addAttributes([QgsField(nomeCampo, tipoCampo, len=comprimento, prec=precisao)])
		layer.updateFields()
		novoIndice = layer.fields().indexOf(nomeCampo)

		layer.startEditing()

		atributos = layer.getFeatures()

		for atributo in atributos:

			idx = atributo.id()
			area = atributo.geometry().area()
			resultado = {novoIndice:(area/10000)}
			provedor.changeAttributeValues({idx:resultado})

		layer.commitChanges()
		
	else:
		print('O campo {} já existe'.format(nomeCampo))

criarCampo('NomeCampo', QVariant.Double, 5, 2)

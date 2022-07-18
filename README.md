# Criar campos geométricos na tabela com PYQGIS

Como criar um campo com valores de área de polígono ou comprimento de linhas no QGIS com PYQGIS

1 - No QGIS, selecione a camada desejada no painel de camadas;

2 - Na linha 21 do script, se desejar calcular o comprimento de uma camada tipo linha, altere o método .area() para .length()

3 - Na linha 30 do script:
- Como primeiro parâmetro da função, coloque entre aspas simples o nome do campo(lembrando de respeitar as limitações de arquivos .shp, sem espaços, caracteres especiais e no máximo 10 caracteres;
- Como segundo parâmetro da função, coloque o tipo do campo, QVariant.Double para números decimais, QVariant.Integer para inteiros e QVariant.String para textos;
- O terceiro e quarto parâmetro da função dizem respeito, respectivamente, ao comprimento e precisão do campo.

### Video aula
[![video aula](https://img.youtube.com/vi/oBogw_nEea8/maxresdefault.jpg)](https://youtu.be/oBogw_nEea8)

var lineCount = 0;
addAddressLine = function () {
    var i = document.createElement('input');
    var x = document.createElement('span');
    var br = document.createElement('br');
    i.setAttribute("type", "text");
    i.id = lineCount;
    x.id=lineCount;
    i.setAttribute("placeholder", "Address Line " + ++lineCount);
    x.textContent='wwww';
    var addressContainer = document.getElementById("adress");

    
    var elemento = document.createElement('span');
    elemento.setAttribute('name', 'nova_materia_' + lineCount);
    elemento.textContent = 'Nova matéria: ';
    
    addressContainer.appendChild(elemento);


    var elemento = document.createElement('span');
    elemento.setAttribute('for', 'titulo_materia_' + lineCount);
    elemento.textContent = 'Nome da matéria: ';

    addressContainer.appendChild(elemento);


    var elemento = document.createElement('input');
    elemento.setAttribute('type', 'text');
    elemento.setAttribute('name', 'titulo_materia_' + lineCount);
    elemento.setAttribute('id', 'titulo_materia_' + lineCount);
    

    addressContainer.appendChild(elemento);
    addressContainer.appendChild(br);
    

    var elemento = document.createElement('span');
    elemento.setAttribute('for', 'assunto_' + lineCount);
    elemento.textContent = 'Assunto:';

    
    addressContainer.appendChild(elemento);

    var elemento = document.createElement('input');
    elemento.setAttribute('type', 'text');
    elemento.setAttribute('name', 'assunto_' + lineCount);
    elemento.setAttribute('id', 'assunto_' + lineCount);

    addressContainer.appendChild(elemento);

    var elemento = document.createElement('span');
    elemento.setAttribute('for', 'descricao_' + lineCount);
    elemento.textContent = 'Descrição:';

    addressContainer.appendChild(elemento);

    var elemento = document.createElement('input');
    elemento.setAttribute('type', 'text');
    elemento.setAttribute('name', 'descricao_' + lineCount);
    elemento.setAttribute('id', 'descricao_' + lineCount);

    addressContainer.appendChild(elemento);

    var elemento = document.createElement('span');
    elemento.setAttribute('for', 'horario_inicio_' + lineCount);
    elemento.textContent = 'Horário de inicio:';
    
    addressContainer.appendChild(elemento);

    var elemento = document.createElement('input');
    elemento.setAttribute('type', 'time');
    elemento.setAttribute('name', 'horario_inicio_' + lineCount);
    elemento.setAttribute('id', 'horario_inicio_' + lineCount);

    addressContainer.appendChild(elemento);

    var elemento = document.createElement('span');
    elemento.setAttribute('for', 'horario_fim_' + lineCount);
    elemento.textContent = 'Horário de termino:';

    addressContainer.appendChild(elemento);

    var elemento = document.createElement('input');
    elemento.setAttribute('type', 'time');
    elemento.setAttribute('name', 'horario_fim_' + lineCount);
    elemento.setAttribute('id', 'horario_fim_' + lineCount);

    addressContainer.appendChild(elemento);

    var elemento = document.createElement('span');
    elemento.setAttribute('for', 'data_materia_' + contador);
    elemento.textContent = 'Data do estudo:';

    addressContainer.appendChild(elemento);

    var elemento = document.createElement('input');
    elemento.setAttribute('type', 'date');
    elemento.setAttribute('name', 'data_materia_' + contador);
    elemento.setAttribute('id', 'data_materia_' + contador);

    addressContainer.appendChild(elemento);

}

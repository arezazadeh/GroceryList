

    const userId = document.getElementById('user').value
    fetch(`/api/list/${userId}`)
    .then(response => response.json())
    .then(function (obj) {
        for (let i = 0; i < obj.length; i++) {
            const parentDiv = document.getElementById('container')
            const rowDiv = document.createElement('div')
            rowDiv.className = "row"
            parentDiv.appendChild(rowDiv)

            const colDivName = document.createElement('div')
            colDivName.className = 'col-9'
            const aTag = document.createElement('a')
            aTag.href = "#"
            aTag.innerHTML = obj[i].name
            colDivName.appendChild(aTag)

            rowDiv.appendChild(colDivName)

            const colDivBtn = document.createElement('div')
            colDivBtn.className = 'col-3'

            rowDiv.appendChild(colDivBtn)

        }
    })
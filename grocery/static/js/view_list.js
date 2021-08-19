fetch("/api/")
.then(function (response){
    if (response.ok) {
        response.json().then(function (data){
            console.log(data)
        })
    }
}) 
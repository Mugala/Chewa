$(document).ready(function(){
    alert("hellp");
    $("form").submit(function(event){
        event.preventDefault();
        var url = document.getElementById('get_answer').getAttribute('action');
        form=$('form')            
        answer=$('input[name={{contents.content}}]:checked').val();
        correct=$('#correct').val();
        if(answer==correct){
            $.ajax({
                'url':url,
                'type':'POST',
                'data':$(this).serialize(),
                'dataType':'json',
                'success': function(response){
                    console.log(response)
                $("#reponse").text(`correct`)
                },
                })              
        }
        else{
            alert("wrong try again!");
        }
       
    
    })
});
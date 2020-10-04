$(function(){
    $('#add_modal').click(function(){
        $('#shadow,#add-modal').removeClass('myself-hide')
    })  


    $('#Ajax_addstu').click(function(){
        $.ajax({
            url:'/modal_add_student/',
            type:'POST',
            data:{
                'name':$('#addname').val(),
                'class':$('#addclass').val()
            },
            success:function(data){
                data =JSON.parse(data) //把字符转换成对象
                if(data.status){
                    location.reload()
                }else{
                    alert(data.message)
                }
            }
        })
    })

    $('#cancle').click(function(){
        $('#shadow,#add-modal').addClass('myself-hide')
    })

    $('.start-edit').click(function(){
        $('#edit-shadow,#edit-modal').removeClass("myself-hide")
        var tds =$(this).parent().prevAll()
        var value_list =[]
        for(var i=0;i<tds.length;i++){
            value_list[i] =$(tds[i]).text()
        }
        stu_id =value_list[3]
        name =value_list[2]
        class_name =value_list[1]
        $("#span_id").text(stu_id)
        $("#edit-name").val(name)
        $("#edit-option").val(class_name)
    })
    $('#edit-cancle').click(function(){
        $('#edit-modal,#edit-shadow').addClass('myself-hide')
    })
    $('#Ajax-edit').click(function(){
        $.ajax({
            url:'/modal_edit_student/',
            type:'POST',
            data:{
                'stu_id' :$("#span_id").text(),
                'new_name':$('#edit-name').val(),
                'new_class':$('#edit-option').val()
            },
            success:function(data){
                data =JSON.parse(data)
                if(data.status){
                    location.href ="/student/"
                }else{
                    alert(data.message)
                }
            }
        })
    })
    $(".start-delete").click(function(){
        $.ajax({
            url:'/modal_del_student/',
            type:'POST',
            data:{
                'stu_id':$(this).val()
            },
            success:function(data){
                data =JSON.parse(data)
                if(data.status){
                    location.href="/student/"
                }else{
                    alert(data.message)
                }
            }
        })
    })
})
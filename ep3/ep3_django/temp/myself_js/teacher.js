$(function(){
    $('.btn-edit').click(function(){
        $('#e-shadow,#e-modal').removeClass("myself-hide")
        var teacher_data =$(this).parent().prevAll()
        $('#e-title').val($(teacher_data[1]).text())
        $('#pid').text($(teacher_data[2]).text())
        var class_list =$(teacher_data[0]).text().split(" ")
        var spanlist =$(teacher_data[0]).find('span')
        var optionlist =$('#eclass_list').find('option')
        for(var i =0;i<spanlist.length;i++){
            for(var j=0;j<optionlist.length;j++){
                if($(optionlist[j]).text() == $(spanlist[i]).text()){
                    $(optionlist[j]).attr("selected","true")
                }
            }
        }
    })



    $('#add_cancle1').click(function(){
        $('#a-shadow,#a-modal').addClass("myself-hide")
    })
    $('.btn-add').click(function(){
        document.getElementById('shadow').classList.remove('myself-hide')
        document.getElementById('modal').classList.remove('myself-hide')
    })
    $('.btn-delete').click(function(){ 
        var tds =$(this).parent().prevAll()
        $.ajax({
            url:'/modal_del_teacher/',
            type:'GET',
            data:{
                'teacher_id':$(tds[2]).text()
            },
            success:function(data){
                location.href="/teacher/"
            }
        })
    })
    $('#e-submit').click(function(){
        var class_list =[]
        $('#eclass_list option:selected').each(function(){
            class_list.push($(this).val())
        })
        $.ajax({
            url:"/modal_edit_teacher/",
            type:'POST',
            traditional:true,
            data:{
                'teacher_id':$('#pid').text().replace("teacher id:",""),
                'teacher_name':$('#e-title').val(),
                'class_list':class_list,
            },
            success:function(data){
                data =JSON.parse(data)
                if(data.status){
                    location.reload()
                }else{
                    alert(data.message)
                }
            }
        })

    })



    $('.btn-add-1').click(function(){
        $("#a-shadow,#loading").removeClass("myself-hide")
        $.ajax({
            url:"/modal_add_1_teacher/",
            type:'GET',
            dataType:'JSON',
            success:function(data){
                $.each(data,function(i,row){
                    //表示juery的循环，data相当于list，i相当于每一项
                    //约等于for row in data 
                    var tag =document.createElement('option')
                    tag.innerHTML =row[1]
                    tag.setAttribute('value',row[0])
                    $('#class_ids').append(tag)
                })
                $("#a-modal").removeClass("myself-hide")
                $('#loading').addClass("myself-hide")
            }
        })
    })




    $("#add_btn1").click(function(){
        var class_list =[]
        $("#class_ids option:selected").each(function(){
            class_list.push($(this).val())
        })
        var teacher=$('#teacher_name_1').val()
        $.ajax({
            url:"/modal_add_teacher/",
            type:"POST",
            data:{
                'title':teacher,
                'class_list':class_list,
            },
            traditional:true,
            success:function(data){
                data =JSON.parse(data)
                if (data.status){
                    location.href='/teacher/';
                }else{
                    $('#error-1').text(data.message);
                }
            }
        })
    })
})


function ecancleModal(){
    document.getElementById('e-shadow').classList.add('myself-hide')
    document.getElementById('e-modal').classList.add('myself-hide')
    $("#eclass_list option:selected").each(function(){
        $(this).removeAttr("selected")
    })
}
function cancleModal(){
    document.getElementById('shadow').classList.add('myself-hide')
    document.getElementById('modal').classList.add('myself-hide')
}
function AjaxSend(){
    var class_list=[]
    $("#class_list option:selected").each(function () {
        class_list.push($(this).val())
    })
    $.ajax({
        url:'/modal_add_teacher/',
        type:'POST',
        data:{
            'title':$('#title').val(),
            'class_list':class_list
        },
        traditional:true,
        success:function(data){
            data =JSON.parse(data)
            if (data.status){
                location.href='/teacher/';
            }else{
                $('#error').text(data.message);
            }

        }
    })
}

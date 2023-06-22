console.log("hello")
var btn = document.getElementsByClassName('add-cart');










function updateOrder(productID, action){
    var url = '/update-cart/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': "application/json",
            
        },
        body:JSON.stringify({'productId':product, 'action':action})
    })
    .then((response) => {
        return response.json()
    })

    .then((message)=>{
        console.log(message)
    })
}


url1 = ' http://127.0.0.1:8000/update-cart/'
url2 = 'http://127.0.0.1:8000/action-cart/'
for (i=0;i<btn.length;i++){
    
    btn[i].addEventListener('click', function (){
        var url = '/update-cart/'
        var product = this.dataset.product
        var action = this.dataset.action


        doSomething(url, product)
        .then((message)=>{
            console.log(message)
        })
    


    }   )
}

for (i=0;i<cart_up.length;i++){
    cart_up[i].addEventListener('click', function (){
        var product = this.dataset.product
        var action = this.dataset.action
        var url = '/action-cart/'
       
       
//         fetch(url, {
//             method:'GET',
//             headers:{
//                 'Content-Type': "application/json",
                
//             },
//             body:JSON.stringify({'cart_itemId':product, 'cart-action':action})
//         })
//         .then((response) => {
//             return response.json()
//         })

//         .then((message)=>{
//             console.log(message)
//         })
//     })
// }
         doSomething(url, product)
         .then((message)=>{
            console.log(message)
         })

function doSomething(uri, itemid){
    return new Promise((resolve, reject)=>{
        fetch(uri, {
            method:'POST',
            headers:{'Content-Type':'application/json', 'X-CSRFToken':token},
            body:JSON.stringify({'item_id':itemid})
        })
        .then((data)=>{
            resolve(data.json())
        })
    })
}


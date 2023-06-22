console.log("hello")
var btn = document.getElementsByClassName('add-cart');
var cart = document.getElementsByClassName('cart-amount')
var close = document.getElementsByClassName('cart-remove')
var checkout = document.getElementById("checkout-btn")
console.log(close)

for(var i=0; i<btn.length; i++){

    btn[i].addEventListener('click', function (){
        var url = ' http://127.0.0.1:8000/update-cart/'
        var product = this.dataset.product
        var action = this.dataset.action

        xhrRequest(url, product, action)
        .then((message)=>{
            console.log(message)
        })


    })
}


for(var i=0; i<cart.length; i++){

    cart[i].addEventListener('click', function(){
        var url = 'http://127.0.0.1:8000/action-cart/'
        var product = this.dataset.product
        var action = this.dataset.action

        xhrCartRequest(url, product, action, i)
        .then((message, i)=>{
            console.log(message)
            cart[i]+= 1
        })
        
    })
}


for(var i=0; i<close.length; i++){

    close[i].addEventListener('click', function (){
        var url = ' http://127.0.0.1:8000/close-cart/'
        var product = this.dataset.product
        var action = this.dataset.action

        xhrRequest(url, product, action)
        .then((message)=>{
            console.log(message)
        })


    })
}

function doSomething(uri, itemid, action){
    return new Promise((resolve, reject)=>{
        fetch(uri, {
            method:'POST',
            headers:{'Content-Type':'application/json', 'X-CSRFToken':token},
            body:JSON.stringify({'item_id':itemid, 'action':action})
        })
        .then((data)=>{
            resolve(data.json())
        })
    })
}

function xhrRequest(url, itemid, action){
    return new Promise((resolve, reject)=>{
        let xhr = new XMLHttpRequest()
        xhr.open('POST', url, true)
        xhr.setRequestHeader('Content-Type', 'application/json')
        data = JSON.stringify({'item_id':itemid})
        xhr.send(data)
        xhr.onload = function(){
            resolve(JSON.parse(this.response))
        }
    })
}

function xhrCartRequest(url, itemid, action, i){
    return new Promise((resolve, reject)=>{
        
        let xhr = new XMLHttpRequest()
        xhr.open('POST', url)
        xhr.setRequestHeader('Content-Type', 'application/json')
        data = JSON.stringify({'item_id':itemid, 'action':action})
        xhr.send(data)
        xhr.onload = function(){
            
            resolve(JSON.parse(this.response))
        }
    })
}

function xhrCheckoutRequest(url, itemid){
    return new Promise((resolve, reject)=>{
        let xhr = new XMLHttpRequest()
        xhr.open('POST', url)
        xhr.setRequestHeader('Content-Type', "application/json")
        data = JSON.stringify({'order_id':itemid})
        xhr.send(data)
        xhr.onload = function (){
             resolve(JSON.parse(this.response))
         }

    })
}

checkout.addEventListener("click", function(){
    let url = ' http://127.0.0.1:8000/checkout-backend/'
    let orderid = this.dataset.order
    xhrCheckoutRequest(url, orderid)
    .then((message)=>{
        console.log(message)
    })
    .then(()=>{
        window.location = ' http://127.0.0.1:8000/'
    })
})
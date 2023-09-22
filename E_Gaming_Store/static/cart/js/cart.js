var updateBtns = document.getElementsByClassName('update-cart');
var cartDiv = document.querySelector('.cart');
var cartItemsNumber = document.querySelector('.circle');
var deleteButtons = document.querySelectorAll('div.delete-div a');
var deleteDivs = document.querySelectorAll('div.delete-div');
var cartItemsDivs = document.querySelectorAll('div.cart-items');
var hrLines = document.querySelectorAll('hr.cart-line');

var deleteButtons2 = document.querySelectorAll('div.main-cart-delete-div a');
var deleteDivs2 = document.querySelectorAll('div.main-cart-delete-div');
var cartItemsDivs2 = document.querySelectorAll('div.item-container');
var hrLines2 = document.querySelectorAll('hr.main-cart-line');

const totalPrice = document.querySelector('.total-price');


for(let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', async function(){
        var product = this.dataset.product
        if(user == 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            data = await updateUserCart(product)
            addToCartOffCanavas(data)
        }
    })
}

async function updateUserCart(product){

    var url = '/cart/update-cart/'

    let data = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'product':product})
    })

   let dataJason =  await data.json()

    return dataJason
}


function addToCartOffCanavas(data){
    // delete div 
    const deleteDiv = document.createElement('div');
    deleteDiv.classList.add('delete-div');

    const deleteDivLink = document.createElement('a');
    deleteDivLink.dataset.cartitem = data["productID"];

    const deleteDivLinkI = document.createElement('i');
    deleteDivLinkI.className = 'fa fa-trash mb-2 delete-item text-light';
    deleteDivLinkI.style.fontSize = '20px';
    deleteDivLinkI.style.width = '20px';

    deleteDivLink.appendChild(deleteDivLinkI);
    deleteDiv.appendChild(deleteDivLink);

    cartDiv.appendChild(deleteDiv)

    //delete Div end 

    // cart Items
    const cartItemsDiv = document.createElement('div');
    cartItemsDiv.className = 'cart-items';


    const img = document.createElement('img');
    img.src = data['image']
    img.className = 'cart-item-img';

    cartItemsDiv.appendChild(img);

    const cartItemsDetailsDiv = document.createElement('div');
    cartItemsDetailsDiv.className = 'ms-2 cart-items-details';

    cartItemsDiv.appendChild(cartItemsDetailsDiv);

    const p1 = document.createElement('p');
    p1.className = 'cart-item-detail';
    p1.innerHTML = 'Name:'+ data['productName'];
    const p2 = document.createElement('p');
    p2.className = 'cart-item-detail';
    p2.innerHTML = 'Price:'+ data['price'];

    cartItemsDetailsDiv.appendChild(p1);
    cartItemsDetailsDiv.appendChild(p2);
    
    cartDiv.appendChild(cartItemsDiv);

    const hr = document.createElement('hr');
    hr.className = 'text-light cart-line';

    cartDiv.appendChild(hr);

    cartItemsNumber.innerHTML = parseInt(cartItemsNumber.innerHTML) + 1;
    alert('Product Added To Cart Successfully!');
    applyDelete();
}

///////////////////////////////////////////////////////////////////
// delete buttons



applyDelete();
function applyDelete(){
    deleteButtons = document.querySelectorAll('div.delete-div a');
    deleteDivs = document.querySelectorAll('div.delete-div');
    cartItemsDivs = document.querySelectorAll('div.cart-items');
    hrLines = document.querySelectorAll('hr.cart-line');

    deleteButtons2 = document.querySelectorAll('div.main-cart-delete-div a');
    deleteDivs2 = document.querySelectorAll('div.main-cart-delete-div');
    cartItemsDivs2 = document.querySelectorAll('div.item-container');
    hrLines2 = document.querySelectorAll('hr.main-cart-line');

    for(let i = 0; i < deleteButtons.length; i++){
        if (deleteButtons[i].getAttribute('listener') !== 'true') 
        {
            deleteButtons[i].setAttribute('listener' , 'true');
            deleteButtons[i].addEventListener('click',  async function(){
                var cartItem = this.dataset.cartitem;
                if(user == 'AnonymousUser'){
                    console.log('Not logged in')
                }else{
                    data = await deleteFromCart(cartItem)
                    if (data['price'])
                    {
                        deleteFromDisplay(i);
                        if (deleteButtons2.length !== 0)
                        {
                            deleteFromDisplayMain(i , data['price']);
                        }
                    }
                    else{
                        alert('An Error Occured! Please try again later.');
                    }
                }
            })
        }
    }    

    for(let i = 0; i < deleteButtons2.length; i++){
        if (deleteButtons2[i].getAttribute('listener') !== 'true') 
        {
            deleteButtons2[i].setAttribute('listener' , 'true');
            deleteButtons2[i].addEventListener('click',  async function(){
                var cartItem = this.dataset.cartitem;
                if(user == 'AnonymousUser'){
                    console.log('Not logged in')
                }else{
                    data = await deleteFromCart(cartItem)
                    if (data['price'])
                    {
                        deleteFromDisplay(i);
                        if (deleteButtons2.length !== 0)
                        {
                            deleteFromDisplayMain(i , data['price']);
                        }
                    }
                    else{
                        alert('An Error Occured! Please try again later.');
                    }
                }
            })
        }
    } 

    
}


async function deleteFromCart(cartItem){
    var url = '/cart/update-cart/'

    let data = await fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'cartItem':cartItem})
    })

    let dataJason = await data.json()

    return dataJason
}

function deleteFromDisplay(index){
    deleteDivs[index].style.display = 'none';
    cartItemsDivs[index].style.display = 'none';
    hrLines[index].style.display = 'none';
    cartItemsNumber.innerHTML = parseInt(cartItemsNumber.innerHTML) - 1;
    alert('Product Removed Successfully!');
}


function deleteFromDisplayMain(index , price){
    deleteDivs2[index].style.display = 'none';
    cartItemsDivs2[index].style.display = 'none';
    hrLines2[index].style.display = 'none';
    console.log(price);
    console.log(price);
    console.log(price);
    totalPrice.innerHTML = String(parseInt(totalPrice.innerHTML) - price);
}





async function onClickDelete(i , data){
    var cartItem = this.dataset.cartitem;
    if(user == 'AnonymousUser'){
        console.log('Not logged in')
    }else{
        data = await deleteFromCart(cartItem)
        if (data['price'])
        {
            deleteFromDisplay(i);
            if (deleteButtons2.length !== 0)
            {
                deleteFromDisplayMain(i , data['price']);
            }
        }
        else{
            alert('An Error Occured! Please try again later.');
        }
    }
}





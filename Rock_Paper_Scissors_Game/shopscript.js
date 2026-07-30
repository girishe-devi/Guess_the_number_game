
let cart=0;

const mycart=document.querySelector('.mycart');
const sales=document.querySelector('.sales-offer')

function openCart(){
    if(cart === 0){
        mycart.classList.remove('mycart-1');
        mycart.innerHTML='<h3>My Cart</h3><button class="close" onclick="closeCart()"><i class="fa-solid fa-xmark"></i></button><div class="cart-container"><div class="cart-item"><img src="./Images/shoe.jpg" alt="Black classy pair Shoes"><div class="item-details"><p>Black classy pair Shoes</p><p>$90.00</p><button class="remove-btn">🗑</button></div></div></div>';

        cart=1;
    }
    else{
        cart=0;
        mycart.innerHTML='';
        mycart.classList.add('mycart-1');
    }
}

function closeCart(){
    console.log(cart);
    if(cart!==0){
        cart=0;
        mycart.innerHTML='';
        mycart.classList.add('mycart-1');
    }
}
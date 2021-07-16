
function shop_selection(){
	const shop_list={"krishna":{"name":"krishna","image":"https://www.evokad.com/wp-content/uploads/2020/04/Post-COVID-Restaurant-Landscape-1-300x300.jpg","location":"karicode"}};
	let list=[];
	let e = document.getElementById('shop'); 
	for (const [key, value] of Object.entries(shop_list)) {
		if(key.startsWith(e.value)  && e.value != ""){
  			list.push(value);
		}
}
document.getElementById("shop_list").innerHTML="";
for(let i=0;i<list.length;i++){
	let a = document.createElement('a');
	a.setAttribute('onclick','show_offers(this)');
	a.setAttribute('name',list[i]['name']);
	let card = document.createElement('div');
	card.setAttribute("class","card");
	let image = document.createElement('img');
	image.setAttribute("src",list[i]['image']);
	let h = document.createElement('h4');
	h.innerHTML=list[i]['name'];
	let p = document.createElement('p');
	p.innerHTML="("+list[i]['location']+")";
	card.appendChild(image);
	card.appendChild(h);
	card.appendChild(p);
	a.appendChild(card);
	document.getElementById("shop_list").appendChild(a);

}

}

function show_offers(argument) {
	const offers = {"offer":"25%","payout":"20 Rs",};
	console.log(argument.name);
	document.getElementById('loginScreen').scroll( 100, 100,);
	for (const [key, value] of Object.entries(offers)) {
		let card = document.createElement('div');
		let h = document.createElement('h4');
		h.innerHTML="";
			
	}
}

setInterval(shop_selection, 1000);

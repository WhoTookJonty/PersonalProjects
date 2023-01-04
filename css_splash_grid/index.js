let columns = Math.floor(document.body.clientWidth / 50),
    rows = Math.floor(document.body.clientHeight / 50);
    
const wrapper = document.getElementById("tiles");

const delay = ms => new Promise(res => setTimeout(res, ms));




let toggled = false;

const handleOnClick = index => 
{
   let tile = document.getElementsByClassName("tile");
   let splash = document.getElementById("splash");

   toggled = !toggled;
  
   for (let i = 0; i < tile.length; i++)
   {
        tile[i].classList.toggle("tile-active");
   }
   if (toggled == false){
        splash.style.animationName = "fadeIn";
        splash.style.animationDuration = "400ms";
        splash.style.animationFillMode = "forwards";
   }else{
        splash.style.animationName = "fadeOut";
        splash.style.animationDuration = "400ms";
        splash.style.animationFillMode = "forwards";
   }
   

    anime({
        targets: ".tile",
        opacity: toggled ? 0 : 1,
        delay: anime.stagger(50, {
            grid: [columns, rows],
            from: index
        })
    });
    
    /*
    const removeWrapper = async () => {
        await delay(1000);
        document.body.removeChild(wrapper);
        document.body.removeChild(splash);
        console.log("waited");
    }
    removeWrapper();
    */
}



const createTile = index => 
{
    const tile = document.createElement("div");

    tile.classList.add("tile");
    tile.classList.add("tile-active");

    tile.onclick = e => handleOnClick(index);
    
    return tile;
}

const createTiles = quantity => 
{
    Array.from(Array(quantity)).map((tile, index) =>
    {
        wrapper.appendChild(createTile(index));
    })
}

createTiles(columns * rows);

const createGrid = () => 
{
    wrapper.innerHTML = "";
    columns = Math.floor(document.body.clientWidth / 50);
    rows = Math.floor(document.body.clientHeight / 50);

    wrapper.style.setProperty("--columns", columns);
    wrapper.style.setProperty("--rows", rows);


    createTiles(columns * rows);
}

window.onload = () => createGrid();
window.onresize = () => createGrid();
let columns = Math.floor(document.body.clientWidth / 50),
    rows = Math.floor(document.body.clientHeight / 50);
    
const wrapper = document.getElementById("tiles");




let toggled = false;

const handleOnClick = index => 
{

   toggled = !toggled;

   //document.body.classList.toggle("toggled"); //not working yet

    anime({
        targets: ".tile",
       opacity: toggled ? 0 : 1,
        delay: anime.stagger(50, {
            grid: [columns, rows],
            from: index
        })
    });
}



const createTile = index => 
{
    const tile = document.createElement("div");

    tile.classList.add("tile");

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
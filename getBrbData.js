// Sample-file for implementing API on page with JS
// Create a div element where you want brb-msg on your page
{/* 
<div id='brb-container'>
    <script> INSERT CODE BELOW HERE </script>
</div> 
*/}


    function renderData(data) {
        const jsondata = JSON.parse(data);
        let brbContainer = document.getElementById('brb-container');
        console.log("data", jsondata);
        console.log("data time", jsondata.return_time);
        console.log("data type", typeof(jsondata));
        if (jsondata.reason) {
            brbContainer.innerHTML = `<h3>Vi är strax tillbaka!</h3><p>För tillfället är vi inte på plats, pga ${jsondata.reason}</p><p>Vi är tillbaka ca:</p><h4>${jsondata.return_time}</h4>`;
        }
        else {
            brbContainer.innerHTML = `<h3>Vi är strax tillbaka!</h3><p>För tillfället är vi inte på plats.</p><p>Vi är tillbaka ca:</p><h4>${jsondata.return_time}</h4>`;
        }        
    }

    async function fetchData() {
        let response = await fetch('https://YOUR_API_URL_HERE');

        console.log(response.status); // 200
        console.log(response.statusText); // OK

        if (response.status === 200) {
            let data = await response.text();            
            if (data) {
                console.log("Data is True");
                renderData(data);
            } else {
                console.log("Data is False");
            }
        }

    }
    fetchData();

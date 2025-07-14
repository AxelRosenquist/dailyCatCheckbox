const checkboxes = ['morning', 'day', 'evening'];

async function fetchCheckboxes(){
    const response = await fetch('/get-state');
    const data = await response.json();
    checkboxes.forEach(checkbox => {
        document.getElementById(checkbox).checked = data[checkbox];
    });
}

setInterval(fetchCheckboxes, 10000);
fetchCheckboxes();

checkboxes.forEach(checkbox => {
    document.getElementById(checkbox).addEventListener('change', async (event) => {
        const state = {}
        checkboxes.map(element => state[element] = document.getElementById(element).checked); 
        await fetch('/set-state', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(state)
        });
    });
});


async function getMatches() {
    const min_safety = document.getElementById("min_safety").value;
    const max_rent = document.getElementById("max_rent").value;
    const min_parks = document.getElementById("min_parks").value;
    const min_walk = document.getElementById("min_walk").value;

    const safety_weight = document.getElementById("safety_weight").value;
    const rent_weight = document.getElementById("rent_weight").value;
    const parks_weight = document.getElementById("parks_weight").value;
    const walk_weight = document.getElementById("walk_weight").value;

    const query = `?safety_weight=${safety_weight}&rent_weight=${rent_weight}&parks_weight=${parks_weight}&walk_weight=${walk_weight}`;

    try {
        const BASE_URL = "https://neighborfit-tk61.onrender.com/";

        fetch(`${BASE_URL}/match?...`)
        const data = await res.json();

        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";

        if (data.length === 0) {
            resultsDiv.innerHTML = "<p>No matching neighborhoods found.</p>";
            return;
        }

        data.forEach(item => {
            const card = document.createElement("div");
            card.className = "card";
            card.innerHTML = `
          <h3>${item.neighborhood}</h3>
          <p>Safety Score: ${item.safety_score}</p>
          <p>Rent: ₹${item.rent}</p>
          <p>Parks Score: ${item.parks_score}</p>
          <p>Walk Score: ${item.walk_score}</p>
          <strong>Match Score: ${item.match_score.toFixed(2)}</strong>
        `;
            resultsDiv.appendChild(card);
        });

    } catch (error) {
        alert("Error fetching data. Is the backend running?");
        console.error(error);
    }
}
  
async function loadDrift() {
    const data = await fetchData("/drift");

    // Summary Cards
    document.getElementById("driftSummary").innerHTML = `
        <div class="card">
            <h3>Drift Score</h3>
            <p>${data.drift_score}/100</p>
        </div>

        <div class="card">
            <h3>Missing Resources</h3>
            <p>${data.missing_count}</p>
        </div>

        <div class="card">
            <h3>Modified Resources</h3>
            <p>${data.modified_count}</p>
        </div>

        <div class="card">
            <h3>Deleted Resources</h3>
            <p>${data.deleted_count}</p>
        </div>

        <div class="card">
            <h3>Status</h3>
            <p>${data.status}</p>
        </div>
    `;

    // Drifted Resources (modified in AWS but not Terraform)
    let driftedHTML = "";

    data.drifted_resources.forEach(item => {
        driftedHTML += `
            <div class="card" style="border-left: 5px solid red;">
                <h4>${item.resource}</h4>
                <p>Terraform: ${item.terraform_state}</p>
                <p>AWS: ${item.live_state}</p>
                <span class="badge red">DRIFT DETECTED</span>
            </div>
        `;
    });

    document.getElementById("driftedList").innerHTML = driftedHTML;

    // Missing resources
    let missingHTML = "";

    data.missing_resources.forEach(item => {
        missingHTML += `
            <div class="card" style="border-left: 5px solid orange;">
                <h4>${item.resource}</h4>
                <p>Present in Terraform but missing in AWS</p>
                <span class="badge yellow">MISSING</span>
            </div>
        `;
    });

    document.getElementById("missingList").innerHTML = missingHTML;
}

loadDrift();
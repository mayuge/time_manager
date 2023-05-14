async function loadCsv() {
    try {
        // ファイルを読み込む
        const file = document.getElementById('fileInput').files[0];
        if (!file) {
            throw new Error('ファイルが選択されていません');
        }
        const content = await new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsText(file, 'shift-jis');
            reader.onload = () => resolve(reader.result);
            reader.onerror = () => reject(reader.error);
        });
        console.log(content);  // 読み込んだ CSV ファイルの内容をコンソールに表示する（デバッグ用）
        // CSV をパースして、HTML のテーブルに表示する
        const lines = content.split('\n');
        const table = document.getElementById('dataTable');
        table.innerHTML = '';
        for (let line of lines) {
            const row = document.createElement('tr');
            const cells = line.split(',');
            for (let cell of cells) {
                const td = document.createElement('td');
                td.textContent = cell;
                row.appendChild(td);
            }
            table.appendChild(row);
        }
    } catch (error) {
        console.error(error);
    }
}

document.getElementById('fileInput').addEventListener('change', loadCsv);

function saveCsv(){
    let eventTitle = document.getElementById('eventTitle').value;
    let startTime = document.getElementById('startTime').value;
    let endTime = document.getElementById('endTime').value;
    let priority = document.getElementById('priority').value;
    let color = document.getElementById('color').value;
    let file =  document.getElementById('fileInput').value;
    
    // CSV形式に変換
    let csvData = `${eventTitle},${startTime},${endTime},${priority},${color}\n`;


}
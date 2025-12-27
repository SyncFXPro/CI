function countItems() {
    const raw = document.getElementById("items").value.trim();
  
    if (!raw) {
      document.getElementById("result").textContent = "0";
      return;
    }
  
    const items = raw
      .split(",")
      .map(i => i.trim())
      .filter(i => i.length > 0);
  
    document.getElementById("result").textContent = items.length;
  }
  
  document.getElementById("items").addEventListener("keydown", e => {
    if (e.key === "Enter") countItems();
  });
  
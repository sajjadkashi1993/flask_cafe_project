const elDashboard = document.getElementById("dashboard")
const elOrders = document.getElementById("orders")
const elTables = document.getElementById("tables")
const elMenuItems = document.getElementById("menu-items")
const elReceipts = document.getElementById("receipts")
const elCharts = document.getElementById("Contact")
const elCategory = document.getElementById("category")


function clickItem(el) {
    const mode = el.target.getAttribute('id').slice(4)
    elDashboard.style.display = mode === "dashboard" ? 'block' : 'none';
    elOrders.style.display = mode === "orders" ? 'block' : 'none';
    elTables.style.display = mode === "tables" ? 'block' : 'none';
    elMenuItems.style.display = mode === "menu-items" ? 'block' : 'none';
    elReceipts.style.display = mode === "receipts" ? 'block' : 'none';
    elCharts.style.display = mode === "Contact" ? 'block' : 'none'
    elCategory.style.display = mode === "category" ? 'block' : 'none'
    if (mode === 'tables'){getTable()}
    if (mode === 'category'){getCategory()}
    if (mode === 'menu-items'){getMenu()}
    if (mode === 'Contact'){getContact()}
    if (mode === 'orders'){getOrders()}
    if (mode === 'receipts'){getReceipts()}
}



document.getElementById("btn-dashboard").onclick = clickItem
document.getElementById("btn-orders").onclick = clickItem
document.getElementById("btn-tables").onclick = clickItem
document.getElementById("btn-category").onclick = clickItem
document.getElementById("btn-menu-items").onclick = clickItem
document.getElementById("btn-receipts").onclick = clickItem
document.getElementById("btn-Contact").onclick = clickItem

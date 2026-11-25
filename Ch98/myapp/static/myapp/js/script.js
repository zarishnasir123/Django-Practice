// The JavaScript (AJAX) code of the product page.
// AJAX = the page talks to the server with JavaScript and changes itself, without reloading.
// The 4 CRUD actions and the request that does each one:
//   Create = POST  /api/products/
//   Read   = GET   /api/products/   (all)   and   GET /api/products/<id>/   (one)
//   Update = PUT   /api/products/<id>/
//   Delete = DELETE /api/products/<id>/

// The address of the JSON views (urls.py). It ends with / like the path in urls.py.
const API_URL = '/api/products/';

// the things of the page that the code needs
const tableBody = document.getElementById('product-table-body');
const form = document.getElementById('product-form');
const nameInput = form.querySelector('[name=name]');
const priceInput = form.querySelector('[name=price]');
const saveBtn = document.getElementById('save-btn');
const cancelBtn = document.getElementById('cancel-btn');

// Django needs the csrf token on every POST, PUT and DELETE. It is in a hidden input of the form ({% csrf_token %}).
const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

// null = we are adding a new product, a number = we are editing the product with that id
let editId = null;


// ---------- READ ----------

// Ask the server for the products (GET) and show them in the table.
// async / await: fetch takes some time, and await waits for the answer without freezing the page.
async function fetchProducts() {
    const response = await fetch(API_URL);        // send the request
    if (response.ok) {                             // ok is true for status 200 to 299
        const products = await response.json();    // the JSON text from JsonResponse becomes a JavaScript array
        showProducts(products);
    } else {
        showMessage('Could not load the products');
    }
}


// One row of the table with a message (used for "no products" and for errors)
function showMessage(text) {
    tableBody.innerHTML = '<tr><td colspan="4" class="text-center text-muted">' + text + '</td></tr>';
}


// A name typed by a user could contain <b> or <script>. This changes the special characters,
// so the browser shows them as text and does not run them.
function escapeHtml(text) {
    return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}


// Put the products in the table, one row for each product
function showProducts(products) {
    if (products.length === 0) {
        showMessage('No products to show yet');
        return;
    }

    let rows = '';
    products.forEach(function (product) {
        // the buttons keep the id of their product in data-id, so we know which one was clicked
        rows += `
            <tr>
                <td>${product.id}</td>
                <td>${escapeHtml(product.name)}</td>
                <td>${product.price}</td>
                <td class="text-end">
                    <button class="btn btn-sm btn-outline-secondary me-1 view-btn" data-id="${product.id}">View</button>
                    <button class="btn btn-sm btn-outline-primary me-1 edit-btn" data-id="${product.id}">Edit</button>
                    <button class="btn btn-sm btn-outline-danger delete-btn" data-id="${product.id}">Delete</button>
                </td>
            </tr>`;
    });
    tableBody.innerHTML = rows;
}


// ---------- CREATE and UPDATE (the Save button) ----------

// The error messages sent by the server (status 400) go under the inputs
function showErrors(errors) {
    // errors looks like {name: ['This field is required.'], price: [...]}
    for (const field in errors) {
        document.getElementById(field + '-error').textContent = errors[field].join(' ');
    }
}

function clearErrors() {
    document.getElementById('name-error').textContent = '';
    document.getElementById('price-error').textContent = '';
}

// Back to the "add a new product" state: empty inputs, Save button, no Cancel button
function resetForm() {
    form.reset();
    editId = null;
    saveBtn.textContent = 'Save';
    cancelBtn.classList.add('d-none');
    clearErrors();
}


// When the form is submitted we do not let the browser reload the page (preventDefault),
// we send the data with fetch instead.
form.addEventListener('submit', async function (event) {
    event.preventDefault();
    clearErrors();

    // the data to send, a JavaScript object
    const data = {
        name: nameInput.value,
        price: priceInput.value
    };

    // a new product = POST to the list url, an old product = PUT to the url with its id
    let url = API_URL;
    let method = 'POST';
    if (editId !== null) {
        url = API_URL + editId + '/';
        method = 'PUT';
    }

    const response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',    // tells the server that the body is JSON
            'X-CSRFToken': csrfToken               // the csrf token goes in this header
        },
        body: JSON.stringify(data)                 // the JavaScript object becomes JSON text
    });

    if (response.ok) {
        resetForm();
        fetchProducts();                           // load the list again, to show the change
    } else {
        const result = await response.json();
        showErrors(result.errors);                 // the form was not valid, show why
    }
});


// ---------- the View, Edit and Delete buttons ----------

// The View button: get that one product (GET one) and show it in the popup
async function viewProduct(id) {
    const response = await fetch(API_URL + id + '/');
    if (!response.ok) {
        alert('This product was not found, maybe it was deleted.');
        fetchProducts();                           // load the list again, to remove it from the table
        return;
    }
    const product = await response.json();

    // textContent writes the text as it is (safe for any name)
    document.getElementById('view-id').textContent = product.id;
    document.getElementById('view-name').textContent = product.name;
    document.getElementById('view-price').textContent = product.price;

    // bootstrap comes from the Bootstrap JavaScript file of base.html
    const popup = bootstrap.Modal.getOrCreateInstance(document.getElementById('view-modal'));
    popup.show();
}


// The Edit button: get that product (GET one) and put its values in the form
async function startEdit(id) {
    const response = await fetch(API_URL + id + '/');
    if (!response.ok) {
        return;
    }
    const product = await response.json();

    nameInput.value = product.name;
    priceInput.value = product.price;
    editId = product.id;                           // from now the Save button does an update
    saveBtn.textContent = 'Update';
    cancelBtn.classList.remove('d-none');
    clearErrors();
}


// The Delete button: ask first, then send DELETE
async function deleteProduct(id) {
    if (!confirm('Delete this product?')) {
        return;
    }

    await fetch(API_URL + id + '/', {
        method: 'DELETE',
        headers: {'X-CSRFToken': csrfToken}
    });

    if (editId === Number(id)) {
        resetForm();                               // the product we were editing is gone
    }
    fetchProducts();
}


// The buttons are made again every time the table is filled, so we do not put a click on each of them.
// One click on the whole table body is enough: event.target tells which button was clicked.
tableBody.addEventListener('click', function (event) {
    const id = event.target.dataset.id;
    if (event.target.classList.contains('view-btn')) {
        viewProduct(id);
    }
    if (event.target.classList.contains('edit-btn')) {
        startEdit(id);
    }
    if (event.target.classList.contains('delete-btn')) {
        deleteProduct(id);
    }
});

cancelBtn.addEventListener('click', resetForm);


// load the products when the page opens
fetchProducts();

// Scrolled
const navbar = document.querySelector(".main-nav");
window.addEventListener("scroll", () => {
  if (window.scrollY > 0) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// Tombol Tambah
const tombolTambah = document.querySelector('#tombol-tambah');
const formTambah = document.querySelector('#form-tambah');
const tombolBatal = document.querySelector('#tombol-batal');
const latarBelakang = document.querySelector('#latar-belakang');

tombolTambah.addEventListener('click', function() {
  formTambah.style.display = 'block';
  latarBelakang.style.display = 'block';
  document.body.style.overflow = 'hidden';
});

tombolBatal.addEventListener('click', function() {
  formTambah.style.display = 'none';
  latarBelakang.style.display = 'none';
  document.body.style.overflow = 'auto';
});

document.querySelector('form').addEventListener('submit', function(e) {
  e.preventDefault();
  // Kode untuk menyimpan data form
  formTambah.style.display = 'none';
  latarBelakang.style.display = 'none';
  document.body.style.overflow = 'auto';
})

function goBack() {
  window.location.reload();
}
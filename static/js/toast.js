function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    if (!toastComponent) return;
  
    // Pastikan ada util class dasar
    toastComponent.classList.add(
      'rounded-lg','border','shadow-lg','px-4','py-3',
      'transition-all','duration-200','transform',
      'fixed','right-6','bottom-6','z-50'
    );
  
    // Hapus kelas tema lama (light) & tema baru (dark) biar nggak numpuk
    toastComponent.classList.remove(
      // light theme lama
      'bg-red-50','border-red-500','text-red-600',
      'bg-green-50','border-green-500','text-green-600',
      'bg-white','border-gray-300','text-gray-800',
      // dark theme baru
      'bg-green-900','border-yellow-500','text-yellow-200',
      'bg-red-900','border-red-500','text-red-100',
      'bg-green-950','border-green-700'
    );
  
    // Terapkan tema sesuai type (match halaman login/register kamu: hijau tua + aksen kuning)
    if (type === 'success') {
      // sukses: hijau tua + border kuning, teks kontras
      toastComponent.classList.add('bg-green-900','border-yellow-500','text-yellow-200');
    } else if (type === 'error') {
      // error: merah tua
      toastComponent.classList.add('bg-red-900','border-red-500','text-red-100');
    } else {
      // normal/info: lebih gelap
      toastComponent.classList.add('bg-green-950','border-green-700','text-yellow-200');
    }
  
    // Isi konten
    toastTitle.textContent = title || '';
    toastMessage.textContent = message || '';
  
    // Tampilkan (animasi naik dari bawah)
    toastComponent.classList.remove('opacity-0','translate-y-64');
    toastComponent.classList.add('opacity-100','translate-y-0');
  
    // Auto-hide
    window.clearTimeout(toastComponent._hideTimer);
    toastComponent._hideTimer = window.setTimeout(() => {
      toastComponent.classList.remove('opacity-100','translate-y-0');
      toastComponent.classList.add('opacity-0','translate-y-64');
    }, duration);
  }
  
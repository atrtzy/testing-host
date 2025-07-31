  <div class="muka" id="muka">😠</div>
  <div class="pesan" id="pesan">Aku lagi ngambek nih!</div>
  <button onclick="ubahMood()">Bujuk aku dong~</button>

  <script>
    function ubahMood() {
      document.getElementById('muka').textContent = '😊';
      document.getElementById('pesan').textContent = 'Yay, udah nggak ngambek lagi!';
    }
  </script>
</body>
</html>

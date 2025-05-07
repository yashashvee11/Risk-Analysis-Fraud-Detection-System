// On doc upload event
var form = document.querySelector("#upload-form");
var fileInput = document.querySelector(".file-input");
var progressArea = document.querySelector(".progress-area");
var uploadedArea = document.querySelector(".uploaded-area");
var csrfToken = document.getElementsByName("csrfmiddlewaretoken");
var loaderWrap = document.querySelector(".loader-wrap");

if (form) {
  form.addEventListener("click", () => {
    console.log('Cliceked on form', form)
    fileInput.click();
  });
  
  fileInput.onchange = ({target})=>{
    let alllowed_mimetypes = ['application/pdf'];
    let allowed_size_mb = 5;

    let files = target.files;
    if (files.length === 0) {
      alert('No file upoaded');
      return
    }
    for (idx=0; idx < files.length; idx++) {
      let file = target.files[idx];
      console.log(file.type);
      if(!alllowed_mimetypes.includes(file.type)) {
        alert('Error: Only pdf files are supported');
        return
      }
      if(file.size <= allowed_size_mb * 1024 * 1024){
        let fileName = file.name;
        if(fileName.length >= 12){
          let splitName = fileName.split('.');
          fileName = splitName[0].substring(0, 13) + "... ." + splitName[1];
        }
        loaderWrap.style.display = 'flex';
        uploadFile(fileName);
      } else {
        alert('Error: file size exceeded for ' + file.name);
        return
      }
    }
    
  }

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  function uploadFile(name){
      let xhr = new XMLHttpRequest();
      xhr.open("POST", "");
      xhr.setRequestHeader("x-requested-with", "XMLHttpRequest")
      xhr.setRequestHeader("x-requested-with", "XMLHttpRequest")
      xhr.upload.addEventListener("progress", ({loaded, total}) =>{
          let fileLoaded = Math.floor((loaded / total) * 100);
          let fileTotal = Math.floor(total / 1000);
          let fileSize;
          (fileTotal < 1024) ? fileSize = fileTotal + " KB" : fileSize = (loaded / (1024*1024)).toFixed(2) + " MB";
          let progressHTML = `<li class="row">
                              <i class="fas fa-file-alt"></i>
                              <div class="content">
                                  <div class="details">
                                  <span class="name">${name} • Uploading</span>
                                  <span class="percent">${fileLoaded}%</span>
                                  </div>
                                  <div class="progress-bar">
                                  <div class="progress" style="width: ${fileLoaded}%"></div>
                                  </div>
                              </div>
                              </li>`;
          uploadedArea.classList.add("onprogress");
          progressArea.innerHTML = progressHTML;
          if(loaded == total){
          progressArea.innerHTML = "";
          let uploadedHTML = `<li class="row">
                                  <div class="content upload">
                                  <i class="fas fa-file-alt"></i>
                                  <div class="details">
                                      <span class="name">${name} • Uploaded</span>
                                      <span class="size">${fileSize}</span>
                                  </div>
                                  </div>
                                  <i class="fas fa-check"></i>
                              </li>`;
          uploadedArea.classList.remove("onprogress");
          uploadedArea.insertAdjacentHTML("afterbegin", uploadedHTML);
          }
      });
      let data = new FormData(form);
      xhr.send(data);

      xhr.onreadystatechange = () => {
        if (xhr.readyState === xhr.HEADERS_RECEIVED) {
          loaderWrap.style.display = 'none';
        }
      };
  }
}

var printBtn = document.querySelector('.print-btn');
if (printBtn) {
  printBtn.addEventListener("click", function(event) {
    window.print()
  });
}

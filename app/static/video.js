function getFrame(){
    const video = document.getElementById('stream')
    const canvas = document.createElement('canvas')
    canvas.width = video.videoWidth
    canvas.height = video.videoHeight
    canvas.getContext('2d').drawImage(video, 0, 0)
    return canvas.toDataURL("image/png")
}

function streamVideo(){
    const video = document.getElementById('stream')
    navigator.mediaDevices.getUserMedia({
        video:{
            height: 300,
            width: 400,
        }
    }).then(stream => video.srcObject = stream)
    setInterval(() => {
        getFrame()
    }, 1000 / 30)
}

document.addEventListener('DOMContentLoaded', streamVideo, false)

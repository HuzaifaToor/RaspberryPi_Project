let monitoring
let wrkg

/**
 * Function to request the server to start the motor
 */
async function requestStartMotor () {
  try {
    // Make request to server
    wrkg = true
    do{
        await axios.post('/start_motor')
        updateStatus('Motor is working untill you press stop Motor ')
        if (monitoring){
            startMonitoring()
        } 
    }
    while(wrkg)
  } catch (e) {
    console.log('Error starting the motor', e)
    updateStatus('Error starting')
  }
}

/** 
 * (Re)start monitoring
 */
async function startMonitoring () {

  monitoring = true
  while (monitoring) {
    let result = await axios.get('/monitor')
    //updateMonitoringData(result.data)
    updateMonitoringData(result.data)
  }
}

/** 
 * Stop monitoring
 */
function stopMonitoring () {
  monitoring = false
}

// Function to stop motor

function stopMotor () {
  wrkg = false
  monitoring = false
}




/**
 * Function to request monitoring data to the server and display it in the main page
 */
function updateMonitoringData (Monitor_result) {

  // Get the HTML element where the status is displayed
  let Monitoring_Data = document.getElementById('monitor_text')
   Monitoring_Data.innerText = JSON.stringify(Monitor_result)
}

/**
 * Function to request the server to stop the motor
 */
async function stopSystem () {
  //...
  try {
  wrkg = false
  //updateStatus('Stopping System')
  await axios.post('/stop_system')
  updateStatus('Stopping System')
  //let result1 = await axios.get('/stop_in_zone')
  updateStatus('System Stopped')
} catch (e) {
    console.log('Error stoping', e)
    updateStatus('Can not stop system....')
}
}
/**
 * Request the server to (not) stop the rod , if it is in the target zone
 */
async function requestStopInZone (cb) {
  try {
    // Update status text
    updateStatus(cb.checked  ? 'Will stop in zone' : 'Will not stop in zone')
    // Request the server to stop the motor in zone
    await axios.post('/stop_in_zone', { stop: cb.checked })
  } catch (e) {
    console.log('Error moving to zone', e)
    updateStatus('Error moving to zone')
  }
}


function updateStatus(statusText) {
  // Get the HTML element where the status is displayed
  let motor_status_text = document.getElementById('status_text')
  motor_status_text.innerText = statusText
}

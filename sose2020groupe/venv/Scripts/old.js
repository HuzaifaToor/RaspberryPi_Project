let monitoring

/**
 * Function to request the server to start the motor
 */
async function requestStartMotor () {
  try {
    // Make request to server
    await axios.post('/start_motor')
    // Update status
    updateStatus('Motor has Moved for given steps')
    startMonitoring()
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
    updateMonitoringData(result.data)
  }
}

/** 
 * Stop monitoring
 */
function stopMonitoring () {
  monitoring = false
}

/**
 * Function to request monitoring data to the server and display it in the main page
 */
function updateMonitoringData () {
  // Get HTML elements where results are displayed
  // ...
}

/**
 * Function to request the server to stop the motor
 */
async function stopMotor () {
  //...
  try {
  updateStatus('Motor stopped')
  await axios.post('/stop_Motor')
  //let result1 = await axios.get('/stop_in_zone')
  updateStatus('Motor stopped')
} catch (e) {
    console.log('Error stoping the motor', e)
    updateStatus('Error stoping')
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

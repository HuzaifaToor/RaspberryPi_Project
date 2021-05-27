let monitoring
let wrkg
let results1

/**
 * Function to request the server to start the motor
 */
async function requestStartMotor () {
  try {
    // This Automatically start Motor and monitoring
    wrkg = true
    monitoring = true
    do{
        updateStatus('Motor started working, Press Stop Motor button to stop')
        await axios.post('/start_motor')
        
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

  let result = await axios.get('/monitor')
   //updateMonitoringData(result.data)
  updateMonitoringData(result.data)

}

/** 
 * Stop monitoring
 */
function stopMonitoring () {
  monitoring = false
  updateStatus('Monitoring Stopped')
}

// Function to stop motor

function stopMotor () {
    //This function will stop Motor Working and monitoring distance and inZone info
    wrkg = false
    updateStatus('Motor will Stop soon')
}




/**
 * Function to request monitoring data to the server and display it in the main page
 */
function updateMonitoringData (Monitor_result) {

  // Get the HTML element where the status is displayed
  const results = JSON.stringify(Monitor_result)
  results1 = JSON.parse(results)
  let Monitoring_Data1 = document.getElementById('distance_text')
  Monitoring_Data1.innerText = results1.distance
  let Monitoring_Data2 = document.getElementById('Inzone_text')
  Monitoring_Data2.innerText = results1.inZone
  
}




/**
 * Request the server to (not) stop the rod , if it is in the target zone
 */
async function requestStopInZone (cb) {
  try {
    // Update status text
    if (cb.checked){
        updateStatus('Will Stop in Zone')
        //await axios.post('/stop_in_zone')
        String(results1.inZone) == "true" ? wrkg=false : wrkg=true

    } else {
        updateStatus('Will not Stop in Zone')
        wrkg = true
    
           }

  } catch (e) {
        console.log('Error moving to zone', e)
        updateStatus('Error moving to zone')
  }
}


/**async function requestStopInZone (cb) {
  try {
    // Update status text
    updateStatus(cb.checked  ? 'Will stop in zone' : 'Will not stop in zone')
    // Request the server to stop the motor in zone
    await axios.post('/stop_in_zone', { stop: cb.checked })
  } catch (e) {
    console.log('Error moving to zone', e)
    updateStatus('Error moving to zone')
  }
}}*/



function updateStatus(statusText) {
  // Get the HTML element where the status is displayed
  let motor_status_text = document.getElementById('status_text')
  motor_status_text.innerText = statusText
}

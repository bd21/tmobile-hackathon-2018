using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PersonBehavior : MonoBehaviour {
    public int state; // 0 - idle, 1 - moving to room, 2 - moving to seat
    public GameObject person;
    public Vector3 target;
    public Rigidbody body;
    public bool manuallyControlled;

	// Use this for initialization
	void Start () {
        manuallyControlled = false;
        person = GetComponent<GameObject>();
        body = GetComponent<Rigidbody>();
        body.freezeRotation = true;
        target = new Vector3(0,0,0);
        
	}
	
	// Update is called once per frame
	void Update () {
        if(!manuallyControlled) {
            if (state == 0) { //idle
                //target = person.transform.position;
                // make lighter?
            }
            else if (state == 1) { // moving to room

            }
            else { //finding seat

            }
        } else {
            // dick around here with the arrow keys.  this also contains xbox code.
            var x = Input.GetAxis("Horizontal") * Time.deltaTime * 1000.0f;
            var z = Input.GetAxis("Vertical") * Time.deltaTime * 1000.0f;

            body.AddForce(x, 0, 0);
            body.AddForce(0, 0, z);
        } 
	}
}

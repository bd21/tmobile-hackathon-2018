using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class PersonBehavior : MonoBehaviour {
    public int state; // 0 - idle, 1 - moving to room, 2 - moving to seat
    public GameObject person;
    public Rigidbody body;
    public bool manuallyControlled;
    //AI
    //[SerializeField]
    public Transform target;
    public NavMeshAgent navMeshAgent;
    // Use this for initialization
    void Start () {
        manuallyControlled = false;
        person = GetComponent<GameObject>();
        body = GetComponent<Rigidbody>();
        body.freezeRotation = true;
        // Pathfinding
        navMeshAgent = this.GetComponent<NavMeshAgent>();

        if(navMeshAgent == null) {
            Debug.LogError("NavMeshAgent is not attached to " + gameObject.name);
        } else {
            SetDestination();
        }
        
        
	}
	
    private void SetDestination() {
        if(target != null) {
            Vector3 targetVector = target.transform.position;
            navMeshAgent.SetDestination(targetVector);
        }
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

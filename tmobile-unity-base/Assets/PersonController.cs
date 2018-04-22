using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PersonController : MonoBehaviour {
    //fields
    [Range(0.0f, 24.0f)]
    public float timeOfDay;
    public enum Capacity {

    }

	// Use this for initialization
	void Start () {
        timeOfDay = 6f;

	}
	
	// Update is called once per frame
	void Update () {
		
	}


}

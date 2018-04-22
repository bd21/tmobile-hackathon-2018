using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SeatController : MonoBehaviour {
    private Collider trigger;
    public GameObject triggerObject;
    private Renderer rend;
    public Color originalColor;
    // Use this for initialization
    void Start () {
        trigger = GetComponent<Collider>();
        rend = GetComponent<Renderer>();
    }
	
	// Update is called once per frame
	void Update () {
		
	}

    void OnTriggerEnter(Collider other) {
        //Debug.Log("enter");
        rend.material.shader = Shader.Find("Specular");
        rend.material.SetColor("_EmissionColor", Color.cyan);

    }

    void OnTriggerExit(Collider other) {
        //Debug.Log("exit");
        rend.material.shader = Shader.Find("Specular");
        rend.material.SetColor("_EmissionColor", originalColor);

    }

}

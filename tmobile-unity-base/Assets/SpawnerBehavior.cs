using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


public class SpawnerBehavior : MonoBehaviour {
    public GameObject spawnedObject;
    public Vector3 size;
    public Vector3 center;
    public GameObject gc;
    GameController script;
    Dictionary<System.DateTime, int> arrivals;
    private int timeInterval;
    List<int> arrivalArray;
    List<System.DateTime> timeArray;
    private int index;
    // Use this for initialization
    void Start () {
        center = transform.position;
        script = gc.GetComponent<GameController>();
        arrivals = script.arrivals;
        arrivalArray = new List<int>();
        timeArray = new List<System.DateTime>();
        if(arrivals == null) {
            Debug.Log("arrivals is null");
        }
        
        foreach (KeyValuePair<System.DateTime, int> entry in arrivals) {
            arrivalArray.Add(entry.Value);
            timeArray.Add(entry.Key);
            //Debug.Log(entry.Value);
        }
        
        timeInterval = 0;
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetKeyDown("n")) {
            Debug.Log("advancing time...");
            Debug.Log("time is now " + timeArray[timeInterval]);
            timeInterval++;
            if(index < arrivalArray.Count) {
                Spawn(arrivalArray[index]);
            }
            
        }
	}

    void Spawn(int quantity) {
        GameObject[] chairs = GameObject.FindGameObjectsWithTag("chair");
        for (int i = 0; i < quantity; i++) {
            Vector3 pos = center + new Vector3(Random.Range(-size.x / 2, size.x / 2),
                                               0,
                                               Random.Range(-size.z / 2, size.z / 2));

            GameObject go = Instantiate(spawnedObject, pos, Quaternion.identity);

            go.GetComponent<NavMeshAgent>().Warp(pos);
            //go.GetComponent<NavMeshAgent>().SetDestination(players[0].transform.position);
            PersonBehavior pb = go.GetComponent<PersonBehavior>();
            //set pb.target - to start, pick a random seat that is unoccupied
            Random r = new Random();
            int number = Random.Range(0, chairs.Length);
            pb.target = chairs[number].transform;

            
        }
    }
}

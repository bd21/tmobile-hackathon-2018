using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System.IO;
using UnityEngine.UI;

public class GameController : MonoBehaviour {
    //fields
    [Range(0.0f, 24.0f)]
    public float timeOfDay;
    public Dictionary<System.DateTime, int> arrivals;
    public Canvas clock;
    public Text roomCounts;
    // Use this for initialization
    void Start() {
        timeOfDay = 6f;
        StartCoroutine(GetStats());
        arrivals = getArrivals();
        

    }

    

    // Update is called once per frame
    void Update() {
        
    }


Dictionary<System.DateTime, int> getArrivals() {
    using (var reader = new StreamReader(@"C:\Users\Blake\Documents\tmobile-hackathon-2018\Arrivals.csv")) {
        Dictionary<System.DateTime, int> result = new Dictionary<System.DateTime, int>();
        int i = 0;
        while (!reader.EndOfStream) {
                var line = reader.ReadLine();
                var values = line.Split(',');

                if (i != 0) {
                    result.Add(System.DateTime.Parse(values[0]), int.Parse(values[1]));
                } else {
                    
                }
                i++;

            }
        
        return result;
    }
}

IEnumerator GetStats() {
        UnityWebRequest www = UnityWebRequest.Get("http://tmobilehack.azurewebsites.net/workspaces");
        yield return www.SendWebRequest();

        if (www.isNetworkError || www.isHttpError) {
            Debug.Log(www.error);
        }
        else {
            // Show results as text
            //  Debug.Log(www.downloadHandler.text);

            // Or retrieve results as binary data
            byte[] results = www.downloadHandler.data;
        }
    }
}




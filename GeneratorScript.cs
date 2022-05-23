using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GeneratorScript : MonoBehaviour
{
    public GameObject roadPrefab;
    public GameObject BuildingPrefab;
    public GameObject GrassPrefab;

    
    // Start is called before the first frame update
    void Start()
    {
        int noOfImages = 3140;
        int imageSize = 1;
        // int imageSize = 1;
        var list = new List<int>(noOfImages);

        for (int i = 0; i < noOfImages; ++i)
            list.Add(0);

        // Random rnd = new Random();

        
        for (int x = 0; x < imageSize; x++)
        {
            for (int y = 0; y < imageSize; y++)
            {
                // int nextImg  = Random.Range(0, noOfImages);
                // while (list[nextImg] == 1){
                //     nextImg = Random.Range(0, noOfImages);
                // }
                int nextImg = 0;
                list[nextImg] = 1;
                // int nextImg = 0;
                string text = System.IO.File.ReadAllText("C:/Users/Jamaica/Desktop/final_text_files_2/map0.txt");
                string[] lines = text.Split('\n');
                float x_img; 
                float.TryParse(lines[0], out x_img);
                float y_img; 
                float.TryParse(lines[1], out y_img);
                float[,] myArray = new float[(int)x_img, (int)y_img];
                for(int k = 0; k < x_img; k++)
                {
                    string lineaux = lines[k+2];
                    string[] line = lineaux.Split(' ');
                    for(int j = 0; j < y_img; j++)
                    {
                        float f; 
                        float.TryParse(line[j], out f);
                        myArray[k, j] = f;
                    }
                }

                for (int i = 0; i < x_img; i++)
                {
                    for (int j = 0; j < y_img; j++)
                    {   
                        
                        if (myArray[i, j] == 0)
                        {
                            GameObject road = Instantiate(roadPrefab, new Vector3(i + imageSize * x, 0, j + imageSize * y), Quaternion.identity);
                            // road.transform.localScale = new Vector3(1, Random.Range(0.75f, 1.5f), 1);
                        }
                        else if (myArray[i, j] == 128)
                        {
                            
                            GameObject building = Instantiate(BuildingPrefab, new Vector3(i + imageSize * x, 0, j + imageSize * y), Quaternion.identity);
                            // building.transform.localScale = new Vector3(1, Random.Range(2, 20), 1);
                            
                        }
                        else if (myArray[i, j] == 255)
                        {
                            GameObject grass = Instantiate(GrassPrefab, new Vector3(i + imageSize * x, 0, j + imageSize * y), Quaternion.identity);
                            // grass.transform.localScale = new Vector3(1, Random.Range(0.75f, 2.25f), 1);
                        }
                    }
                }
            }
        }
        
        
    }
}

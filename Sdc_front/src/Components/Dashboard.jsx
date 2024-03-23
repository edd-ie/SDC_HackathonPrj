import React, { useEffect, useRef } from "react";
import { useState } from "react";
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, LabelList, Label } from "recharts";
import './Dashboard.css'




export default function Dashboard() {
    const [data, setData] = useState([])
    const [flip, setFlip] = useState(false)
    const [future, setFuture] = useState(true)

    function handleData(e) {
        
        let button = e.target;
        let name = button.innerText;
        let idName = button.id;
        let parent = button.parentElement;
        for (let i = 0; i < parent.children.length; i++) {
            parent.children[i].className = "switch"
        }
        console.log(name, button.className, idName);
        button.className = "switch active"

        fetch(`http://localhost:5000/sector/${idName}`)
        .then(res => res.json())
        .then(data => {

            const dataArray = Object.entries(data).map(([name, value]) => ({
                name,
                emissions: value.emission,
                offset: value.offset
                })
            );
            console.log(dataArray);
            setData(dataArray);
        })
        
    }


    useEffect(() => {
        fetch(`http://localhost:5000/sector/total`)
        .then(res => res.json())
        .then(data => {

            const dataArray = Object.entries(data).map(([name, value]) => ({
                name,
                emissions: value.emission,
                offset: value.offset
                })
            );
            console.log(dataArray);
            setData(dataArray);
        })
    },[])

    function handleShift(e) {
        let button = e.target;
        let name = button.innerText;
        let idName = button.id;
        let parent = button.parentElement;
        
        setFlip(idName!="visual" ? true : false)
        if(idName =="visual"){
           fetch(`http://localhost:5000/sector/total`)
            .then(res => res.json())
            .then(data => {

                const dataArray = Object.entries(data).map(([name, value]) => ({
                    name,
                    emissions: value.emission,
                    offset: value.offset
                    })
                );
                console.log(dataArray);
                setData(dataArray);
            })
        }
        
        for (let i = 0; i < parent.children.length; i++) {
            parent.children[i].className = "bars"
        }
        console.log(name, button.className, idName);
        button.className = "bars activeBar"

        setFuture(idName=="pred" ? true : false)
        if(idName == "pred"){
            fetch(`http://localhost:5000/prediction`)
            .then(res => res.json())
            .then(data => {
                console.log(data);
                const dataArray = Object.entries(data).map(([name, value]) => ({
                    name,
                    emissions: value.toFixed(2)
                    })
                );
                console.log(dataArray);
                setData(dataArray);
            })
        }
    }

   const Table = ({ data }) => {
        return (
            <table>
            <thead>
                <tr>
                <th>Sector</th>
                <th>Company</th>
                <th>Offset</th>
                <th>Cost</th>
                <th>Quantity</th>
                <th>Emission Left</th>
                </tr>
            </thead>
            <tbody>
                {data.map((item) => (
                <tr key={item.password}>
                    <td>{item.firstname}</td>
                    <td>{item.lastname}</td>
                    <td>{item.email}</td>
                    <td>{item.password}</td>
                    <td>{item.sector}</td>
                    <td>{item.company}</td>
                    <td>{item.offset}</td>
                    <td>{item.cost}</td>
                    <td>{item.quantity}</td>
                    <td>{item.left}</td>
                </tr>
                ))}
            </tbody>
            </table>
        );
    };



    return (
    <div className="Dashboard">

        <div className="head">Irvine Carbon Dataset</div>
        
        {!flip ? 
        <div className="folder">
            <AreaChart className="chart" width={700} height={250} data={data}
            margin={{ top: 10, right: 0, left: 0, bottom: 0 }}>
            <defs>
                <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#8884d8" stopOpacity={0.9}/>
                <stop offset="95%" stopColor="#8884d8" stopOpacity={0}/>
                </linearGradient>
                <linearGradient id="colorPv" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#82ca9d" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#82ca9d" stopOpacity={0}/>
                </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Area type="monotone" dataKey="emissions" stroke="#8884d8" fillOpacity={1} fill="url(#colorUv)" />
            <Area type="monotone" dataKey="offset" stroke="#82ca9d" fillOpacity={1} fill="url(#colorPv)" />
            </AreaChart>

            <h3 className="Label">Sector Emissions</h3>
            
            <div className="tabs">
                <div id="total" className="switch active" onClick={handleData} >Total</div>
                <div id="agriculture" className="switch" onClick={handleData}>Agriculture</div>
                <div id="aviation" className="switch" onClick={handleData} >Aviation</div>
                <div id="commercial" className="switch" onClick={handleData} >Commercial</div>
                <div id="energy" className="switch" onClick={handleData} >Energy</div>
                <div id="forestry" className="switch" onClick={handleData} >Forestry</div>
                <div id="industrial" className="switch" onClick={handleData} >Industrial</div>
                <div id="marine" className="switch" onClick={handleData} >Marine</div>
                <div id="residential" className="switch" onClick={handleData} >Residential</div>
                <div id="transportation" className="switch" onClick={handleData} >Transportation</div>
                <div id="waste" className="switch" onClick={handleData} >Waste</div>
            </div>
        </div>
        : 
            <div className="folder">
                {future ? 
                    <>
                        <AreaChart className="chart" width={700} height={250} data={data}
                        margin={{ top: 10, right: 0, left: 0, bottom: 0 }}>
                            <Label value="Pages of my website" offset={0} position="top" />
                            <defs>
                                <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#8884d8" stopOpacity={0.9}/>
                                <stop offset="95%" stopColor="#8884d8" stopOpacity={0}/>
                                </linearGradient>
                                <linearGradient id="colorPv" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#82ca9d" stopOpacity={0.8}/>
                                <stop offset="95%" stopColor="#82ca9d" stopOpacity={0}/>
                                </linearGradient>
                                
                            </defs>
                            <XAxis dataKey="name" />
                            
                            <YAxis />
                            <CartesianGrid strokeDasharray="3 3" />
                            <Tooltip />
                            <Area type="monotone" dataKey="emissions" stroke="#8884d8" fillOpacity={1} fill="url(#colorUv)" />
                            <Area type="monotone" dataKey="offset" stroke="#82ca9d" fillOpacity={1} fill="url(#colorPv)" />
                        </AreaChart>
                        <h3 className="Label">2024 Forecasted Sector Emissions</h3>
                    </>

                : <div></div>}
            </div>
        }

        <div className="sidebar">
            <div className="bars" id="visual" onClick={handleShift}>
                <span className="material-symbols-sharp">
                monitoring
                </span> Visualize
            </div>
            <div className="bars" id="pred" onClick={handleShift}>
                <span className="material-symbols-sharp">
                emoji_objects
                </span> Predictions
            </div>
            <div className="bars" id="invest" onClick={handleShift}>
                <span className="material-symbols-sharp">
                monetization_on
                </span> Investments
            </div>
        </div>
        
    </div>
  ); 
}

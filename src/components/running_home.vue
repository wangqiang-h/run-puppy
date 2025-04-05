<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="time">9:41</span></div>
          </div>
          <div class="dynamic-island">
            <div class="status-bar-dynamic-island">
              <div class="true-depth-camera"></div>
              <div class="facetime-camera"></div>
            </div>
          </div>
          <div class="right-side">
            <div class="signal-wifi-battery">
              <div class="icon-mobile-signal"></div>
              <div class="wifi"></div>
              <div class="status-bar-battery"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame">
        <div class="frame-1" @click="goToRunning"><div class="vector"></div></div>
        <span class="details">Details</span>
        <div class="frame-2">
          <div class="frame-3">
            <div class="ellipse"></div>
            <div class="ellipse-4"></div>
            <div class="ellipse-5"></div>
          </div>
        </div>
      </div>
      <div class="ellipse-6"></div>
      <div class="vector-7"><div class="mask-group"></div></div>
      <div class="ellipse-8"></div>
      <div class="dog"></div>
      <div class="small-house"></div>
      <span class="now">now</span>
      <div class="vector-9"><span class="home">HOME</span></div>
      <div class="mask-group-a"></div>
      <div class="rectangle">
        <div class="rectangle-b"></div>
        <div class="flex-row-dff">
          <span class="real-time-location">Real-time location</span>
          <div class="frame-c"><div class="layer"></div></div>
        </div>
        <div class="flex-row-aea">
          <div class="address"></div>
          <span class="sukabumi-indonesia">Sukabumi,Indonesia</span>
          <div class="union"></div>
          <span class="a-little-tired">A little tired 💤</span>
        </div>
        <span class="familiar-area">your pet is in a familiar area.</span>
        <div class="flex-row-cd">
          <div class="frame-d">
            <div class="flex-column-edfe">
              <div class="calories"></div>
              <div class="ellipse-e"></div>
            </div>
            <div class="flex-column-dc">
              <span class="calorie-consumption">Calorie<br />consumption</span>
              <div class="kcal">
                <span class="kcal-value">1700</span
                ><span class="kcal-f">Kcal</span>
              </div>
            </div>
          </div>
          <div class="frame-10">
            <div class="flex-column">
              <div class="route"></div>
              <div class="ellipse-11"></div>
            </div>
            <div class="flex-column-12">
              <span class="running-distance">Running <br />distance</span>
              <div class="m">
                <span class="dot">1.200</span><span class="m-13">m</span>
              </div>
            </div>
          </div>
        </div>
        <div class="frame-14">
<div @click="goToHome"></div> 
<div @click="goToNearby"></div> 
<div @click="goToRunning"></div>
<div @click="goToshop"></div> 
        </div>
        <div class="home-indicator"></div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goToRunning = () => {
  router.push({ name: 'running' });
};
const goToHome  = () => {
  router.push({ name: 'home' });
};
const goToNearby  = () => {
  router.push({ name: 'nearby' });
};
const goToshop  = () => {
  router.push({ name: 'shop' });
};

</script>
  
  <style scoped>
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
    "Source Han Sans CN", sans-serif;
}

.main-container {
  overflow: hidden;
}

.main-container,
.main-container * {
  box-sizing: border-box;
}

input,
select,
textarea,
button {
  outline: 0;
}

.main-container {
  position: relative;
  width: 393px;
  height: 852px;
  margin: 0 auto;
  background: #1d1e20;
  overflow: hidden;
}
.top-navigation {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  background: #1d1e20;
  backdrop-filter: blur(10px);
}
.status-bar {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 1;
}
.left-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 0 3px 10px;
  z-index: 2;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.time {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 54px;
  height: 20px;
  top: 1px;
  left: 0;
  color: #ffffff;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.dynamic-island {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 125px;
  min-height: 0;
  z-index: 5;
}
.status-bar-dynamic-island {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.true-depth-camera {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 7;
  overflow: hidden;
  border-radius: 100px;
}
.facetime-camera {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 8;
  overflow: hidden;
  border-radius: 100px;
}
.right-side {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 11px 0 0;
  z-index: 9;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.frame {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 94px;
  position: relative;
  width: 351px;
  margin: 12px 0 0 21px;
  z-index: 43;
}
.frame-1 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 51px;
  height: 51px;
  padding: 19px 21px 19px 21px;
  background: #ffffff;
  z-index: 44;
  border-radius: 25.5px;
}
.vector {
  flex-shrink: 0;
  position: relative;
  width: 11px;
  height: 15px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/back-arrow.svg)
    no-repeat center;
  background-size: cover;
  z-index: 45;
}
.details {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 61px;
  height: 22px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 600;
  line-height: 21.784px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 46;
}
.frame-2 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 51px;
  height: 51px;
  padding: 13px 24px 13px 24px;
  background: #ffffff;
  z-index: 47;
  border-radius: 25.5px;
}
.frame-3 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 3px;
  position: relative;
  width: 3px;
  z-index: 48;
}
.ellipse {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/ellipse-dot-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 49;
  border-radius: 50%;
}
.ellipse-4 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/ellipse-dot-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 50;
  border-radius: 50%;
}
.ellipse-5 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/ellipse-dot-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 51;
  border-radius: 50%;
}
.ellipse-6 {
  position: absolute;
  width: 273px;
  height: 273px;
  top: 135px;
  left: 57px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/outer-circle.svg)
    no-repeat center;
  background-size: cover;
  z-index: 15;
  border-radius: 50%;
}
.vector-7 {
  position: absolute;
  width: 238.129px;
  height: 123.104px;
  top: 161.372px;
  left: 83.726px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/map-path-top.svg)
    no-repeat center;
  background-size: cover;
  z-index: 20;
}
.mask-group {
  position: relative;
  width: 22px;
  height: 22px;
  margin: 16.628px 0 0 94.274px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/mask-group-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 56;
}
.ellipse-8 {
  position: absolute;
  width: 167px;
  height: 167px;
  top: 188px;
  left: 110px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/inner-circle.svg)
    no-repeat center;
  background-size: cover;
  z-index: 16;
  border-radius: 50%;
}
.dog {
  position: absolute;
  width: 28px;
  height: 20px;
  top: 246px;
  left: 62px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/dog-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 22;
  overflow: hidden;
}
.small-house {
  position: absolute;
  width: 43px;
  height: 43px;
  top: 250px;
  left: 50%;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/house-icon.svg)
    no-repeat center;
  background-size: cover;
  transform: translate(-31.4%, 0);
  z-index: 17;
  overflow: hidden;
}
.now {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 20px;
  height: 1.29%;
  top: 31.69%;
  left: calc(50% - 130.5px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 9.147541046142578px;
  font-weight: 600;
  line-height: 11px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 19;
}
.vector-9 {
  position: absolute;
  width: 234.804px;
  height: 187.973px;
  top: 276.819px;
  left: 76.188px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/map-path-bottom.svg)
    no-repeat center;
  background-size: cover;
  z-index: 21;
}
.home {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 28px;
  height: 5.85%;
  top: 6.48%;
  left: calc(50% - 2.59px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 9.147541046142578px;
  font-weight: 600;
  line-height: 11px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 18;
}
.mask-group-a {
  position: absolute;
  width: 33px;
  height: 30.211px;
  top: 330px;
  left: 291px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/mask-group-secondary.png)
    no-repeat center;
  background-size: cover;
  z-index: 55;
}
.rectangle {
  position: absolute;
  width: 393px;
  height: 696px;
  top: 449.819px;
  left: 0;
  background: #ffffff;
  z-index: 23;
  border-radius: 33px 33px 0 0;
}
.rectangle-b {
  position: relative;
  width: 99px;
  height: 2px;
  margin: 14px 0 0 147px;
  background: #d9d9d9;
  z-index: 52;
  border-radius: 1.5px;
}
.flex-row-dff {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 364px;
  height: 44px;
  margin: 23.181px 0 0 16px;
  z-index: 26;
}
.real-time-location {
  flex-shrink: 0;
  position: relative;
  height: 24px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 25;
}
.frame-c {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 44px;
  height: 44px;
  padding: 2px 7px 2px 7px;
  background: #eeeeeb;
  z-index: 26;
  overflow: hidden;
  border-radius: 43px;
}
.layer {
  flex-shrink: 0;
  position: relative;
  width: 33px;
  height: 27px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/layer-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 27;
}
.flex-row-aea {
  position: relative;
  width: 368px;
  height: 28.181px;
  margin: -4.181px 0 0 12px;
  z-index: 32;
}
.address {
  position: absolute;
  width: 22px;
  height: 21px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/address-pin.svg)
    no-repeat center;
  background-size: cover;
  z-index: 28;
  overflow: hidden;
}
.sukabumi-indonesia {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 141px;
  height: 17px;
  top: 2.181px;
  left: 23px;
  color: #ff5218;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 29;
}
.union {
  position: absolute;
  width: 87px;
  height: 23.139px;
  top: 5.042px;
  left: 281px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/speech-bubble.svg)
    no-repeat center;
  background-size: cover;
  z-index: 31;
}
.a-little-tired {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 65px;
  height: 12px;
  top: 13.181px;
  left: 293px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 10px;
  font-weight: 500;
  line-height: 12px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.2px;
  z-index: 32;
}
.familiar-area {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: relative;
  width: 144px;
  height: 13px;
  margin: -3.181px 0 0 16px;
  color: #848484;
  font-family: Inter, var(--default-font-family);
  font-size: 10.705883026123047px;
  font-weight: 500;
  line-height: 12.957px;
  text-align: center;
  white-space: nowrap;
  z-index: 30;
}
.flex-row-cd {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 364px;
  height: 102px;
  margin: 10px 0 0 16px;
  z-index: 38;
}
.frame-d {
  flex-shrink: 0;
  position: relative;
  width: 172px;
  height: 102px;
  background: #eeeeee;
  z-index: 33;
  border-radius: 19px;
}
.flex-column-edfe {
  position: absolute;
  width: 44px;
  height: 33px;
  top: 9.181px;
  left: 109px;
  z-index: 37;
}
.calories {
  position: relative;
  width: 23px;
  height: 23px;
  margin: 10px 0 0 10px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/calories-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 37;
  overflow: hidden;
}
.ellipse-e {
  position: absolute;
  width: 44px;
  height: 44px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/calories-circle.svg)
    no-repeat center;
  background-size: cover;
  z-index: 34;
  border-radius: 50%;
}
.flex-column-dc {
  position: absolute;
  width: 94px;
  height: 73px;
  top: 19px;
  left: 19px;
  font-size: 0px;
  z-index: 36;
}
.calorie-consumption {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: relative;
  width: 85px;
  height: 34px;
  margin: 0 0 0 0;
  color: #a19d9d;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-overflow: initial;
  letter-spacing: -0.28px;
  z-index: 35;
  overflow: hidden;
}
.kcal {
  position: relative;
  width: 94px;
  height: 29px;
  margin: 10px 0 0 0;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
  text-overflow: initial;
  white-space: nowrap;
  z-index: 36;
}
.kcal-value {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.kcal-f {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.frame-10 {
  flex-shrink: 0;
  position: relative;
  width: 171px;
  height: 102px;
  background: #eeeeee;
  z-index: 38;
  border-radius: 19px;
}
.flex-column {
  position: absolute;
  width: 44px;
  height: 36px;
  top: 9.181px;
  left: 111px;
  z-index: 42;
}
.route {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 8px 0 0 8px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/route-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 42;
  overflow: hidden;
}
.ellipse-11 {
  position: absolute;
  width: 44px;
  height: 44px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/distance-circle.svg)
    no-repeat center;
  background-size: cover;
  z-index: 39;
  border-radius: 50%;
}
.flex-column-12 {
  position: absolute;
  width: 80px;
  height: 73px;
  top: 19px;
  left: 19px;
  font-size: 0px;
  z-index: 41;
}
.running-distance {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: relative;
  width: 57px;
  height: 34px;
  margin: 0 0 0 0;
  color: #a19d9d;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-overflow: initial;
  letter-spacing: -0.28px;
  z-index: 40;
  overflow: hidden;
}
.m {
  position: relative;
  width: 80px;
  height: 29px;
  margin: 10px 0 0 0;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
  text-overflow: initial;
  white-space: nowrap;
  z-index: 41;
}
.dot {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.m-13 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.frame-14 {
  position: relative;
  width: 364px;
  height: 87px;
  margin: 21.181px 0 0 16px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183259/bottom-frame-background.png)
    no-repeat center;
  background-size: cover;
  z-index: 24;
  border-radius: 29.5px;
  display: flex; 
}
.frame-14 > div {
            width: 25%;
            height: 100%;
            cursor: pointer;
        }
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 52px 0 0 130px;
  background: #000000;
  z-index: 54;
  border-radius: 100px;
}

</style>
  
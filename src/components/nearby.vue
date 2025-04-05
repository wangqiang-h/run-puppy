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
    <div class="flex-row">
      <span class="matches">matches</span>
      <div class="message-reminder"></div>
    </div>
    <div class="flex-row-a">
      <div class="rectangle"><div class="etc"></div></div>
      <div class="rectangle-1"><span class="all">all</span></div>
      <div class="rectangle-2"><span class="new">new</span></div>
      <div class="rectangle-3"><span class="nearby">nearby</span></div>
    </div>
    <div class="flex-row-c">
      <div class="image">
        <div class="flex-row-4">
          <div class="ellipse"></div>
          <span class="online">online</span>
        </div>
        <span class="pupu">pupu</span
        ><span class="usa-california">USA.California</span>
        <div class="flex-row-5">
          <div class="rectangle-6">
            <div class="rectangle-7"><div class="error"></div></div>
          </div>
          <div class="rectangle-8"></div>
          <div class="rectangle-9"><div class="heart"></div></div>
          <div class="chat"></div>
        </div>
      </div>
      <div class="image-a">
        <div class="image-b">
          <div class="rectangle-c">
            <span class="she-likes-you">she likes you!</span>
            <div class="vector"></div>
          </div>
        </div>
      </div>
      <div class="image-d">
        <div class="flex-row-d">
          <div class="ellipse-e"></div>
          <span class="online-f">online</span>
        </div>
        <span class="pupu-10">pupu</span
        ><span class="usa-california-11">USA.California</span>
        <div class="flex-row-fa">
          <div class="rectangle-12">
            <div class="rectangle-13"><div class="error-14"></div></div>
          </div>
          <div class="rectangle-15"></div>
          <div class="rectangle-16"><div class="heart-17"></div></div>
          <div class="chat-18"></div>
        </div>
      </div>
      <div class="image-19">
        <div class="flex-row-d-1a">
          <div class="ellipse-1b"></div>
          <span class="online-1c">Online</span>
        </div>
        <div class="flex-row-c-1d">
          <div class="pupu-1e"></div>
          <span class="pupu-1f">pupu</span>
        </div>
        <div class="flex-row-a-20">
          <div class="rectangle-21"></div>
          <div class="address"></div>
          <span class="china-shanghai">china.shanghai</span>
        </div>
        <div class="flex-row-c-22">
          <div class="rectangle-23"><div class="group"></div></div>
          <div class="rectangle-24"><div class="chat-25"></div></div>
          <div class="rectangle-26"><div class="heart-27"></div></div>
        </div>
      </div>
    </div>
    <div class="frame">
      <div @click="goToHome"></div> 
<div @click="goToNearby"></div> 
<div @click="goToRunning"></div>
<div @click="goToshop"></div> 
    </div>
    <div class="home-indicator"></div>
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
  background: linear-gradient(180deg, #fffcda, #ffffff);
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
  color: #000000;
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
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.flex-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 346px;
  height: 60px;
  margin: 24px 0 0 27px;
  z-index: 19;
}
.matches {
  flex-shrink: 0;
  position: relative;
  height: 40px;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 33.26422882080078px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 19;
}
.message-reminder {
  flex-shrink: 0;
  position: relative;
  width: 60px;
  height: 60px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/message-reminder-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 18;
  overflow: hidden;
}
.flex-row-a {
  position: relative;
  width: 346px;
  height: 54px;
  margin: 5px 0 0 27px;
  z-index: 24;
}
.rectangle {
  position: absolute;
  width: 70px;
  height: 54px;
  top: 0;
  left: 0;
  background: #ffe99b;
  z-index: 20;
  border-radius: 32px;
}
.etc {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 18px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/etc-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 27;
  overflow: hidden;
}
.rectangle-1 {
  position: absolute;
  width: 70px;
  height: 54px;
  top: 0;
  left: 77px;
  background: #ffe99b;
  z-index: 21;
  border-radius: 32px;
}
.all {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 15px;
  left: 23px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 26;
}
.rectangle-2 {
  position: absolute;
  width: 79px;
  height: 54px;
  top: 0;
  left: 155px;
  background: #ff5218;
  z-index: 22;
  border-radius: 32px;
}
.new {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 15px;
  left: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 23;
}
.rectangle-3 {
  position: absolute;
  width: 104px;
  height: 54px;
  top: 0;
  left: 242px;
  background: #ffe99b;
  z-index: 24;
  border-radius: 32px;
}
.nearby {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 15px;
  left: 19px;
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
.flex-row-c {
  position: relative;
  width: 1041px;
  height: 465px;
  margin: 29px 0 0 -323px;
  z-index: 55;
}
.image {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/profile-image-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 55;
  border-radius: 20px;
}
.flex-row-4 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 56px;
  height: 17px;
  margin: 298px 0 0 23px;
  z-index: 62;
}
.ellipse {
  flex-shrink: 0;
  position: relative;
  width: 7px;
  height: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/online-status-ellipse.svg)
    no-repeat center;
  background-size: cover;
  z-index: 62;
  border-radius: 50%;
}
.online {
  flex-shrink: 0;
  position: relative;
  height: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 57;
}
.pupu {
  display: block;
  position: relative;
  height: 40px;
  margin: -3px 0 0 21px;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 33.26422882080078px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 56;
}
.usa-california {
  display: block;
  position: relative;
  height: 17px;
  margin: 0 0 0 23px;
  color: #707070;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 58;
}
.flex-row-5 {
  position: relative;
  width: 296px;
  height: 53px;
  margin: 5px 0 0 21px;
  z-index: 63;
}
.rectangle-6 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 0;
  background: #ffffff;
  z-index: 59;
  border-radius: 10px;
}
.rectangle-7 {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 11px 0 0 30px;
  background: #000000;
  z-index: 66;
  overflow: visible auto;
  border-radius: 5px;
}
.error {
  position: relative;
  width: 18px;
  height: 19px;
  margin: 5px 0 0 5px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/error-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 67;
  overflow: hidden;
}
.rectangle-8 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 104px;
  background: #ffffff;
  opacity: 0.5;
  z-index: 60;
  border-radius: 10px;
}
.rectangle-9 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 208px;
  background: #ff5218;
  z-index: 61;
  border-radius: 10px;
}
.heart {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 28px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/heart-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 64;
  overflow: hidden;
}
.chat {
  position: absolute;
  width: 15.2%;
  height: 84.91%;
  top: 7.55%;
  left: 42.57%;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/chat-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 63;
  overflow: hidden;
}
.image-a {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 350px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/profile-image-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 29;
}
.image-b {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/profile-image-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 30;
  border-radius: 20px;
}
.rectangle-c {
  position: relative;
  width: 155px;
  height: 27px;
  margin: 16px 0 0 21px;
  background: #ff5218;
  z-index: 69;
  border-radius: 13.5px;
}
.she-likes-you {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 19px;
  top: 5px;
  left: 32px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 70;
}
.vector {
  position: absolute;
  width: 9.03%;
  height: 48.15%;
  top: 29.63%;
  left: 8.39%;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/vector-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 71;
}
.image-d {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 702px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/profile-image-4.png)
    no-repeat center;
  background-size: cover;
  z-index: 41;
  border-radius: 20px;
}
.flex-row-d {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 56px;
  height: 17px;
  margin: 298px 0 0 23px;
  z-index: 48;
}
.ellipse-e {
  flex-shrink: 0;
  position: relative;
  width: 7px;
  height: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/online-status-ellipse-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 48;
  border-radius: 50%;
}
.online-f {
  flex-shrink: 0;
  position: relative;
  height: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 43;
}
.pupu-10 {
  display: block;
  position: relative;
  height: 40px;
  margin: -3px 0 0 21px;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 33.26422882080078px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 42;
}
.usa-california-11 {
  display: block;
  position: relative;
  height: 17px;
  margin: 0 0 0 23px;
  color: #707070;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 44;
}
.flex-row-fa {
  position: relative;
  width: 296px;
  height: 53px;
  margin: 5px 0 0 21px;
  z-index: 49;
}
.rectangle-12 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 0;
  background: #ffffff;
  z-index: 45;
  border-radius: 10px;
}
.rectangle-13 {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 11px 0 0 30px;
  background: #000000;
  z-index: 52;
  overflow: visible auto;
  border-radius: 5px;
}
.error-14 {
  position: relative;
  width: 18px;
  height: 19px;
  margin: 5px 0 0 5px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/error-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 53;
  overflow: hidden;
}
.rectangle-15 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 104px;
  background: #ffffff;
  opacity: 0.5;
  z-index: 46;
  border-radius: 10px;
}
.rectangle-16 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 208px;
  background: #ff5218;
  z-index: 47;
  border-radius: 10px;
}
.heart-17 {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 28px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/heart-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 50;
  overflow: hidden;
}
.chat-18 {
  position: absolute;
  width: 15.2%;
  height: 84.91%;
  top: 7.55%;
  left: 42.57%;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/chat-icon-2.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 49;
  overflow: hidden;
}
.image-19 {
  position: absolute;
  width: 314px;
  height: 414px;
  top: 51px;
  left: 362px;
  background: #fff9c0;
  z-index: 17;
  border-radius: 20px;
}
.flex-row-d-1a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 55px;
  height: 17px;
  margin: 234px 0 0 9px;
  z-index: 76;
}
.ellipse-1b {
  flex-shrink: 0;
  position: relative;
  width: 7px;
  height: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/online-status-ellipse-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 36;
}
.online-1c {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 43px;
  height: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 76;
}
.flex-row-c-1d {
  position: relative;
  width: 83px;
  height: 40px;
  margin: -2px 0 0 7px;
  z-index: 32;
  overflow: visible auto;
}
.pupu-1e {
  position: relative;
  width: 78.087px;
  height: 30.996px;
  margin: 7.501px 0 0 2.386px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/pupu-background.svg)
    no-repeat center;
  background-size: cover;
  z-index: 31;
}
.pupu-1f {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 40px;
  top: 0;
  left: 0;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 33.27004623413086px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 32;
}
.flex-row-a-20 {
  position: relative;
  width: 122px;
  height: 23px;
  margin: 2px 0 0 9px;
  z-index: 75;
}
.rectangle-21 {
  position: absolute;
  width: 122px;
  height: 23px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/address-background.svg)
    no-repeat center;
  background-size: cover;
  z-index: 73;
}
.address {
  position: absolute;
  width: 18px;
  height: 17px;
  top: 3px;
  left: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/address-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 74;
  overflow: hidden;
}
.china-shanghai {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 80px;
  height: 13px;
  top: 5px;
  left: 28px;
  color: #707070;
  font-family: Inter, var(--default-font-family);
  font-size: 10.633182525634766px;
  font-weight: 500;
  line-height: 12.869px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 75;
}
.flex-row-c-22 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 296px;
  height: 53px;
  margin: 9px 0 0 9px;
  z-index: 35;
}
.rectangle-23 {
  flex-shrink: 0;
  position: relative;
  width: 88px;
  height: 53px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/rectangle-button-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 33;
}
.group {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 11px 0 0 30px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/group-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 39;
}
.rectangle-24 {
  flex-shrink: 0;
  position: relative;
  width: 88px;
  height: 53px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/rectangle-button-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 34;
}
.chat-25 {
  position: relative;
  width: 45px;
  height: 45px;
  margin: 4px 0 0 22px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/chat-icon-3.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 37;
  overflow: hidden;
}
.rectangle-26 {
  flex-shrink: 0;
  position: relative;
  width: 88px;
  height: 53px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/rectangle-button-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 35;
}
.heart-27 {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 28px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/heart-icon-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 38;
  overflow: hidden;
}
.frame {
  position: relative;
  width: 364px;
  height: 87px;
  margin: 40px 0 0 16px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184521/bottom-frame.png)
    no-repeat center;
  background-size: cover;
  z-index: 14;
  border-radius: 29.5px;
  display: flex; 

}
.frame > div {
            width: 25%;
            height: 100%;
            cursor: pointer;
        }
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 16px 0 0 130px;
  background: #000000;
  z-index: 16;
  border-radius: 100px;
}


</style>

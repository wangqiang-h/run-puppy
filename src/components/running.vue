<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="edit-time">9:41</span></div>
          </div>
          <div class="dynamic-island">
            <div class="status-bar-1">
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
      <div class="rectangle" :style="{ visibility: showText ? 'visible' : 'hidden' }"  @click="goToRunningDetails">
        <div class="group"></div>
        <div class="group-2"></div>
        <div class="flex-column-a">
          <span class="date-request">Date request</span
          ><span class="your-dog">Your Dog</span><span class="hansen">Hansen</span
          ><span class="accrept-request">Accrept request? </span>
        </div>
      </div>
      <div class="img-4"></div>
      <div class="frame">
        <div class="frame-3"><div class="fi-sr-paw"></div></div>
        <span class="get-started" @click="goToRunningHome">get started</span>
      </div>
      <div class="home-indicator"></div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goToRunningHome = () => {
  router.push({ name: 'running_home' });
};

const goToRunningDetails = () => {
  router.push({ name: 'running_details' });
};

import { ref, onMounted } from 'vue'

const showText = ref(false)
let hasSet = false // 标记是否已经设置过

function setShowText(value) {
  if (!hasSet && value === true) {
    showText.value = true
    hasSet = true
  }
}

onMounted(() => {
  setTimeout(() => {
    setShowText(true) // 只能成功设置一次 true
  }, 2000)
})

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
  background: linear-gradient(180deg, #fffbd7, #fffefe);
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
.edit-time {
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
.status-bar-1 {
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
  background: url(https://static.codia.ai/custom_image/2025-04-05/183530/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183530/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183530/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.rectangle {
  position: relative;
  width: 365px;
  height: 135px;
  margin: 23px 0 0 14px;
  background: #ffe99b;
  z-index: 21;
  border-radius: 45px;
}
.group {
  position: absolute;
  width: 81px;
  height: 86px;
  top: 24px;
  left: 260px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183530/dog-illustration.png)
    no-repeat center;
  background-size: cover;
  z-index: 23;
}
.group-2 {
  position: absolute;
  width: 80px;
  height: 80px;
  top: 28px;
  left: 18px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183530/profile-avatar.png)
    no-repeat center;
  background-size: cover;
  z-index: 22;
  border-radius: 50%;
}
.flex-column-a {
  position: absolute;
  width: 120px;
  height: 78px;
  top: 30px;
  left: 111px;
  font-size: 0px;
  z-index: 27;
}
.date-request {
  display: block;
  position: relative;
  height: 14px;
  margin: 0 0 0 0;
  color: #6f83ff;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14px;
  text-align: left;
  white-space: nowrap;
  z-index: 26;
}
.your-dog {
  display: block;
  position: relative;
  height: 14px;
  margin: 5px 0 0 0;
  color: #7e7e7e;
  font-family: Inter, var(--default-font-family);
  font-size: 12.882630348205566px;
  font-weight: 600;
  line-height: 14px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 25;
}
.hansen {
  display: block;
  position: relative;
  height: 25px;
  margin: 0 0 0 0;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 22.3073787689209px;
  font-weight: 600;
  line-height: 24.538px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 24;
}
.accrept-request {
  display: block;
  position: relative;
  height: 17px;
  margin: 3px 0 0 0;
  color: #8e8e8e;
  font-family: Inter, var(--default-font-family);
  font-size: 14.571428298950195px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  white-space: nowrap;
  z-index: 27;
}
.img-4 {
  position: relative;
  width: 206px;
  height: 240px;
  margin: 113px 0 0 108px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183530/main-dog-image.png)
    no-repeat center;
  background-size: cover;
  z-index: 28;
}
.frame {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 65px;
  position: relative;
  width: 334px;
  height: 59px;
  margin: 158px 0 0 30px;
  padding: 5px 6px 5px 6px;
  background: #ff5218;
  z-index: 16;
  border-radius: 29.5px;
}
.frame-3 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 75px;
  height: 48px;
  padding: 13px 27px 13px 27px;
  background: #000000;
  z-index: 17;
  border-radius: 24px;
}
.fi-sr-paw {
  flex-shrink: 0;
  position: relative;
  width: 21px;
  height: 21px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/183530/paw-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 18;
  overflow: hidden;
}
.get-started {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 114px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 500;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 19;
}
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 52px 0 0 130px;
  background: #000000;
  z-index: 15;
  border-radius: 100px;
}

</style>
  
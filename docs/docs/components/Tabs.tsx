import React, { useState, Children } from 'react';
import styles from './Tabs.module.css';

interface TabPaneProps {
  children?: React.ReactNode;
  label: React.ReactNode;
  icon?: React.ReactNode;
}

interface TabsProps {
  children: React.ReactNode;
  defaultValue?: number;
  className?: string;
}

type TabsComponent = React.FC<TabsProps> & {
  TabPane: React.FC<TabPaneProps>;
};

const Tabs: TabsComponent = ({ children, defaultValue = 0, className = '' }) => {
  const safeInitial = (() => {
    const arr = Children.toArray(children).filter(React.isValidElement) as React.ReactElement<TabPaneProps>[];
    if (arr.length === 0) return 0;
    const dv = typeof defaultValue === 'number' ? defaultValue : 0;
    return Math.min(Math.max(dv, 0), arr.length - 1);
  })();

  const [activeTab, setActiveTab] = useState<number>(safeInitial);

  const childrenArray = Children.toArray(children).filter(React.isValidElement) as React.ReactElement<TabPaneProps>[];

  return (
    <div className={`${styles.tabsContainer} ${className}`}>
      <div className={styles.tabsList}>
        {childrenArray.map((child, index) => {
          const { label, icon } = child.props;
          return (
            <button
              key={index}
              className={`${styles.tabTrigger} ${activeTab === index ? styles.active : ''}`}
              onClick={() => setActiveTab(index)}
              type="button"
            >
              {icon && <span className={styles.tabIcon}>{icon}</span>}
              {label}
            </button>
          );
        })}
      </div>

      <div className={styles.tabContent}>
        {childrenArray.map((child, index) => (
          <div
            key={index}
            className={`${styles.tabPane} ${activeTab === index ? styles.active : ''}`}
            aria-hidden={activeTab !== index}
          >
            {activeTab === index && child.props.children}
          </div>
        ))}
      </div>
    </div>
  );
};

const TabPane: React.FC<TabPaneProps> = ({ children }) => {
  return <>{children}</>;
};

Tabs.TabPane = TabPane;

export default Tabs;

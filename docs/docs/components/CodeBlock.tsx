import React, { useState } from 'react';
import { Highlight, themes } from 'prism-react-renderer';
import styles from './CodeBlock.module.css';
import { Language } from 'prism-react-renderer';

const vsDark = themes.vsDark;

interface CodeBlockProps {
  children: string;
  language?: Language | string;
  title?: string;
  showCopy?: boolean;
  className?: string;
}

const CodeBlock: React.FC<CodeBlockProps> = ({
  children,
  language = 'bash',
  title,
  showCopy = true,
  className = '',
}): React.ReactElement => {
  const [copyText, setCopyText] = useState<string>('Copy');
  const [copyIcon, setCopyIcon] = useState<string>('📋');

  const handleCopy = async (): Promise<void> => {
    const textToCopy = children ?? '';
    if (typeof navigator === 'undefined' || !navigator.clipboard?.writeText) {
      setCopyText('Unavailable');
      setCopyIcon('❌');
      setTimeout(() => {
        setCopyText('Copy');
        setCopyIcon('📋');
      }, 2000);
      return;
    }

    try {
      await navigator.clipboard.writeText(textToCopy);
      setCopyText('Copied!');
      setCopyIcon('✅');

      setTimeout(() => {
        setCopyText('Copy');
        setCopyIcon('📋');
      }, 2000);
    } catch {
      setCopyText('Failed');
      setCopyIcon('❌');
      setTimeout(() => {
        setCopyText('Copy');
        setCopyIcon('📋');
      }, 2000);
    }
  };

  return (
    <div className={`${styles.codeBlock} ${className}`}>
      <div className={styles.codeHeader}>
        <div className={styles.codeLanguage}>{title ?? String(language).toUpperCase()}</div>
        {showCopy && (
          <button
            type="button"
            className={styles.copyButton}
            onClick={handleCopy}
            aria-label="Copy code"
          >
            <span>{copyIcon}</span>
            <span>{copyText}</span>
          </button>
        )}
      </div>

      <div className={styles.codeContent}>
        <Highlight code={children.trim()} language={String(language) as Language} theme={vsDark}>
          {({ className: highlightClass, style, tokens, getLineProps, getTokenProps }) => (
            <pre className={`${highlightClass} ${styles.pre}`} style={style}>
              <code className={styles.codeInner}>
                {tokens.map((line, i) => (
                  <div key={i} {...getLineProps({ line, key: i })} className={styles.line}>
                    {line.map((token, key) => (
                      <span key={key} {...getTokenProps({ token, key })} />
                    ))}
                  </div>
                ))}
              </code>
            </pre>
          )}
        </Highlight>
      </div>
    </div>
  );
};

export default CodeBlock;
